from suds.client import Client
from suds.cache import DocumentCache
from pathlib import Path

class SATApi:

    def __init__(self):
        # cache the information of this service
        wsdl = "https://consultaqr.facturaelectronica.sat.gob.mx/consultacfdiservice.svc?wsdl"
        # I chose DocumentCache because schemas are stored in a human-readable xml format
        cache_path = Path(__file__).parent / "cache"
        self._client = Client(wsdl, cache=DocumentCache(location=cache_path))

    def verify_cfdi(self, uuid, rfc_emisor, rfc_receptor, total_facturado):
        # build string
        args = f"re={rfc_emisor}&rr={rfc_receptor}&tt={total_facturado}&id={uuid}"
        # call web service
        raw_response = self._client.service.Consulta(args)
        # map to a plain dictionary to hide suds implementation
        return self._response_to_dict(raw_response)
    
    def _response_to_dict(self, raw_response) -> dict:
        response = dict()
        for key, value in dict(raw_response).items():
            response[key] = str(value) if value else None
        return response