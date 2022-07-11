from cfdibills.api import SATConsultaResponse, consulta_cfdi_service
from cfdibills.cfdis.cfdi33 import CFDI33
from cfdibills.cfdis.complementos import TimbreFiscalDigital


def verify(
    cfdi: CFDI33 = None,
    uuid: str = None,
    rfc_emisor: str = None,
    rfc_receptor: str = None,
    total_facturado: float = None,
) -> SATConsultaResponse:
    """
    Verifies a bill's status with the SAT. The bill can be given as a CFDI33 or as its details (uuid, rfc_emisor,
    rfc_receptor, total_facturado).

    Parameters
    ----------
    cfdi
    uuid
    rfc_emisor
    rfc_receptor
    total_facturado

    Returns
    -------
    SATConsultaResponse
    """
    # this is validated in _verify_cfdi_by_values
    return (
        _verify_cfdi(cfdi)
        if cfdi
        else _verify_cfdi_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)  # type: ignore
    )


def _verify_cfdi(cfdi: CFDI33) -> SATConsultaResponse:
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
