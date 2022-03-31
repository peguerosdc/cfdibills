from .api import sat_api
from .parsing import normalize_dict_keys
from .utils import get_uuid

def verify(cfid: dict = None,
    uuid: str = None,
    rfc_emisor: str = None, rfc_receptor: str = None,
    total_facturado: float = None) -> dict:
    """
    
    """
    # if an object was passed, try to verify it as a cfid
    # else, try to verify item by item
    return _verify_cfid(cfid) if cfid else _verify_cfid_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)

def _verify_cfid(cfid: dict) -> dict:
    # get required items from the cfid object
    rfc_emisor = cfid["emisor"]["rfc"]
    rfc_receptor = cfid["receptor"]["rfc"]
    total_facturado = cfid["total"]
    # look for uuid
    uuid = get_uuid(cfid)
    # verify cfid with sat
    return _verify_cfid_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)

def _verify_cfid_by_values(uuid: str, rfc_emisor: str, rfc_receptor: str, total_facturado: str) -> dict:
    # validate that arguments are valid
    if uuid is None or rfc_emisor is None or rfc_receptor is None or total_facturado is None:
        raise ValueError("All args [uuid, rfc_emisor, rfc_receptor, total_facturado] must be not None")
    # call web service
    raw_response = sat_api.verify_cfdi(uuid, rfc_emisor, rfc_receptor, total_facturado)
    return normalize_dict_keys(raw_response)