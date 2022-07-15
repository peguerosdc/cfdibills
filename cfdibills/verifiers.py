"""
Module to verify a CFDI with the SAT.
"""
from typing import Union

from cfdibills.api import SATConsultaResponse, consulta_cfdi_service
from cfdibills.schemas.cfdi33 import CFDI33
from cfdibills.schemas.cfdi40 import CFDI40
from cfdibills.schemas.complementos import TimbreFiscalDigital


def verify(
    cfdi: Union[CFDI33, CFDI40] = None,
    uuid: str = None,
    rfc_emisor: str = None,
    rfc_receptor: str = None,
    total_facturado: float = None,
) -> SATConsultaResponse:
    """
    Verifies a bill's status with the SAT. The bill can be given as a ``CFDI33`` or as its details (uuid, rfc_emisor,
    rfc_receptor, total_facturado).

    When the ``CFDI33`` is present, no other detail is used to query the SAT's web service. If the ``CFDI33`` is not
    present, then all the other details must be provided.

    Parameters
    ----------
    cfdi: CFDI33
        CFDI v3.3 object to check. Details are overriden by this argument when passed.
    uuid: str
        UUID of the CFDI to check (if details are given).
    rfc_emisor: str
        RFC of the issuer of the CFDI to check (if details are given).
    rfc_receptor: str
        RFC of the recipient of the CFDI to check (if details are given).
    total_facturado: str
        Total amount of money billed in the CFDI to check (if details are given).

    Returns
    -------
    SATConsultaResponse
        Status of the CFDI as verified by SAT.

    Raises
    ------
    ValueError
        When no CFDI is provided or there are missing details.
    """
    return (
        _verify_cfdi(cfdi)
        if cfdi
        # this is validated in _verify_cfdi_by_values
        else _verify_cfdi_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)  # type: ignore
    )


def _verify_cfdi(cfdi: Union[CFDI33, CFDI40]) -> SATConsultaResponse:
    return _verify_cfdi_by_values(
        str(cfdi.get_complemento(TimbreFiscalDigital).uuid),
        cfdi.emisor.rfc,
        cfdi.receptor.rfc,
        cfdi.total,
    )


def _verify_cfdi_by_values(
    uuid: str, rfc_emisor: str, rfc_receptor: str, total_facturado: float
) -> SATConsultaResponse:
    if uuid is None or rfc_emisor is None or rfc_receptor is None or total_facturado is None:
        raise ValueError("All args [uuid, rfc_emisor, rfc_receptor, total_facturado] must be not None")
    return consulta_cfdi_service(uuid, rfc_emisor, rfc_receptor, total_facturado)
