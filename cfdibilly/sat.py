from cfdibilly.api import sat_api
from cfdibilly.utils.parsing import normalize_dict_keys
from cfdibilly.utils.cfdiutils import get_uuid

def verify(cfdi: dict = None,
    uuid: str = None,
    rfc_emisor: str = None, rfc_receptor: str = None,
    total_facturado: float = None) -> dict:
    """
    Verifies a CFDI's status with SAT

    Args:
        cfid: a dict with the structure of a CFDI, or
        uuid, rfc_emisor, rfc_receptor, total_facturado: the required metadata of a CFDI
    """
    # if an object was passed, try to verify it as a CFDI
    # else, try to verify item by item
    return _verify_cfdi(cfdi) if cfdi else _verify_cfdi_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)

def _verify_cfdi(cfdi: dict) -> dict:
    """
    Verifies a CFDI's dict status with SAT

    Args:
        cfdi: a dict with the structure of a CFDI
    """
    # get required items from the cfid object
    rfc_emisor = cfdi["emisor"]["rfc"]
    rfc_receptor = cfdi["receptor"]["rfc"]
    total_facturado = cfdi["total"]
    # look for uuid
    uuid = get_uuid(cfdi)
    # verify cfdi with sat
    return _verify_cfdi_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)

def _verify_cfdi_by_values(uuid: str, rfc_emisor: str, rfc_receptor: str, total_facturado: str) -> dict:
    """
    Verifies a CFDI's status with SAT given its metadata

    Args:
        uuid: folio fiscal of the CFDI
        rfc_emisor: RFC of the CFDI's emitter
        rfc_receptor: RFC of the CFDI's receiver
        total_facturado: total amount of the CFDI
    """
    # validate that arguments are valid
    if uuid is None or rfc_emisor is None or rfc_receptor is None or total_facturado is None:
        raise ValueError("All args [uuid, rfc_emisor, rfc_receptor, total_facturado] must be not None")
    # call web service
    raw_response = sat_api.verify_cfdi(uuid, rfc_emisor, rfc_receptor, total_facturado)
    return normalize_dict_keys(raw_response)