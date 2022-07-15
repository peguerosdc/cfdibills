import datetime
from collections import namedtuple
from dataclasses import dataclass

import pytest
from pytest import mark

from cfdibills.errors import ComplementoNotFoundError
from cfdibills.schemas import Aerolineas, Impuesto, TimbreFiscalDigital
from cfdibills.schemas.mixins import CFDIMixin
from tests.utils import does_not_raise


@dataclass
class DummyTax:
    impuesto: Impuesto
    importe: float


@dataclass
class DummyCFDI(CFDIMixin):
    complemento = [
        TimbreFiscalDigital(
            version="1.1",
            uuid="41acc53c-4fac-405a-8671-f60eb554548e",
            fecha_timbrado=datetime.datetime.now(),
            rfc_prov_certif="rfc_prov_certif",
            sello_cfd="sello_cfd",
            no_certificado_sat="no_certificado_sat",
            sello_sat="sello_sat",
        )
    ]


def generate_dummy_cfdi(with_taxes: bool = True):
    dummy = DummyCFDI()
    if with_taxes:
        taxes = {
            "traslados": [
                DummyTax(impuesto=Impuesto.iva, importe=50),
                DummyTax(impuesto=Impuesto.iva, importe=20),
                DummyTax(impuesto=Impuesto.ieps, importe=20),
            ],
            "retenciones": [
                DummyTax(impuesto=Impuesto.iva, importe=50),
                DummyTax(impuesto=Impuesto.isr, importe=20),
            ],
        }
        dummy.impuestos = namedtuple("Impuestos", taxes.keys())(*taxes.values())  # type: ignore
    else:
        dummy.impuestos = None
    return dummy


@mark.parametrize(
    "dummy, tax, amount",
    [
        (generate_dummy_cfdi(), Impuesto.iva, 70),
        (generate_dummy_cfdi(), Impuesto.ieps, 20),
        (generate_dummy_cfdi(), Impuesto.isr, 0),
        (generate_dummy_cfdi(with_taxes=False), Impuesto.iva, 0),
    ],
)
def test_total_transferred_tax(dummy, tax: Impuesto, amount: float):
    assert dummy.get_total_transferred_tax(tax) == amount


@mark.parametrize(
    "dummy, tax, amount",
    [
        (generate_dummy_cfdi(), Impuesto.iva, 50),
        (generate_dummy_cfdi(), Impuesto.ieps, 0),
        (generate_dummy_cfdi(), Impuesto.isr, 20),
        (generate_dummy_cfdi(with_taxes=False), Impuesto.iva, 0),
    ],
)
def test_total_withheld_tax(dummy, tax: Impuesto, amount: float):
    assert dummy.get_total_withheld_tax(tax) == amount


@mark.parametrize(
    "complemento_type, raises",
    [
        (TimbreFiscalDigital, does_not_raise()),
        (Aerolineas, pytest.raises(ComplementoNotFoundError)),
    ],
)
def test_get_complemento(complemento_type, raises):
    dummy = DummyCFDI()
    with raises:
        complemento = dummy.get_complemento(complemento_type)
        assert isinstance(complemento, complemento_type)
