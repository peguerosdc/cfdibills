"""
Mixins to be used with CFDIs.
"""

from typing import List, Optional, Protocol, Type

from cfdibills.errors import ComplementoNotFoundError
from cfdibills.schemas.catalogs import Impuesto
from cfdibills.schemas.complementos import AnyComplementoType, ComplementoType
from cfdibills.schemas.fields import NonNegativeSixDecimals


class _SingleTaxProto(Protocol):
    impuesto: Impuesto
    importe: NonNegativeSixDecimals


class _ImpuestosProto(Protocol):
    traslados: List[_SingleTaxProto]
    retenciones: List[_SingleTaxProto]


class CFDIMixin:
    """
    Behavior to be extended by a CFDI. This mixin is meant to be used with any version of CFDI.
    """

    # Type stubs are used to tell mypy to expect these attrs to exist.
    # See: https://mypy.readthedocs.io/en/stable/protocols.html#defining-subprotocols-and-subclassing-protocols
    #: Type stub of CFDIx.impuestos
    impuestos: Optional[_ImpuestosProto]
    #: Type stub of CFDIx.complemento
    complemento: List[ComplementoType] = []

    def get_total_transferred_tax(self, tax_type: Impuesto) -> float:
        """
        Computes the total tax transferred (from ``impuestos.traslados``) of type ``tax_type``.

        Parameters
        ----------
        tax_type: Impuesto
            Type of tax to sum.

        Returns
        -------
        float
            Sum of all the transferred taxes of type ``tax_type``.
        """
        taxes = self.impuestos.traslados if self.impuestos else []
        return sum([tax.importe for tax in taxes if tax.impuesto == tax_type])

    def get_total_withheld_tax(self, tax_type: Impuesto) -> float:
        """
        Computes the total tax get_total_withheld_tax (from ``impuestos.retenciones``) of type ``tax_type``.

        Parameters
        ----------
        tax_type: Impuesto
            Type of tax to sum.

        Returns
        -------
        float
            Sum of all the withheld taxes of type ``tax_type``.
        """
        taxes = self.impuestos.retenciones if self.impuestos else []
        return sum([tax.importe for tax in taxes if tax.impuesto == tax_type])

    def get_complemento(self, complemento_type: Type[AnyComplementoType]) -> AnyComplementoType:
        """
        Retrieves the complemento of type ``complemento_type``.

        Parameters
        ----------
        complemento_type: Type[AnyComplementoType]
            Type of complemento to find.

        Returns
        -------
        AnyComplementoType
            Complemento found in this CFDI of type ``complemento_type``

        Raises
        -------
        ComplementoNotFoundError
            When the CFDI doesn't contain a complemento of type ``complemento_type``
        """
        for complemento in self.complemento:
            if isinstance(complemento, complemento_type):
                return complemento
        raise ComplementoNotFoundError(f"This CFDI has no {complemento_type.__name__}")
