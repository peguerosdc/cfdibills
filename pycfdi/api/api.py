from suds.client import Client

class SATApi:

    def __init__(self):
        wsdl = "https://consultaqr.facturaelectronica.sat.gob.mx/consultacfdiservice.svc?wsdl"
        self._client = Client(wsdl)

    def verify_cfdi(self, uuid, rfc_emisor, rfc_receptor, total_facturado):
        # build string
        args = f"re={rfc_emisor}&rr={rfc_receptor}&tt={total_facturado}&id={uuid}"
        # call web service
        raw_response = self._client.service.Consulta(args)
        # map to a plain dictionary to hide suds implementation
        response = dict()
        for key, value in dict(raw_response).items():
            response[key] = str(value) if value else None
        return response