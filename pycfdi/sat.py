from .api import sat_api
from .utils import normalize_dict_keys

def verify(cfid: dict = None,
    uuid: str = None,
    rfc_emisor: str = None, rfc_receptor: str = None,
    total_facturado: float = None):
    # if an object was passed, try to verify it as a cfid
    # else, try to verify item by item
    return _verify_cfid(cfid) if cfid else _verify_cfid_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)

def _verify_cfid(cfid: dict):
    # get required items from the cfid object
    rfc_emisor = cfid["emisor"]["rfc"]
    rfc_receptor = cfid["receptor"]["rfc"]
    total_facturado = cfid["total"]
    # look for uuid
    uuid = None
    for complement in cfid["complemento"]:
        timbres = complement.get("timbre_fiscal_digital", [])
        for timbre in timbres:
            if "uuid" in timbre:
                uuid = timbre["uuid"]
    # verify cfid with sat
    return _verify_cfid_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado)

def _verify_cfid_by_values(uuid, rfc_emisor, rfc_receptor, total_facturado):
    # TODO validate
    # call web service
    raw_response = sat_api.verify_cfdi(uuid, rfc_emisor, rfc_receptor, total_facturado)
    return normalize_dict_keys(raw_response)