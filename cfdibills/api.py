from dataclasses import dataclass

import requests
import xmltodict


@dataclass
class SATConsultaResponse:
    """
    Encloses the response of the ConsultaCFDIService web service when called with a Consulta action
    """

    codigo_estatus: str
    es_cancelable: str
    estado: str
    estatus_cancelacion: str
    validacion_efos: str


def _call_sat(uuid: str, rfc_emisor: str, rfc_receptor: str, total_facturado: float) -> dict:
    """
    Sends a SOAP request to SAT's web service to get the status of a CFDI

    Parameters
    ----------
    uuid
    rfc_emisor
    rfc_receptor
    total_facturado

    Returns
    -------
    A dictionary with the parse response from SAT
    """
    body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
        <soapenv:Header/>
        <soapenv:Body>
            <tem:Consulta>
                <!--Optional:-->
                <tem:expresionImpresa>
                    <![CDATA[?re={rfc_emisor}&rr={rfc_receptor}&tt={total_facturado}&id={uuid}]]>
                </tem:expresionImpresa>
            </tem:Consulta>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    url = "https://consultaqr.facturaelectronica.sat.gob.mx/ConsultaCFDIService.svc?wsdl"
    headers = {
        "content-type": 'text/xml;charset="utf-8"',
        "SOAPAction": "http://tempuri.org/IConsultaCFDIService/Consulta",
    }
    response = requests.post(url, data=body, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"An error occurred when verifying with SAT. Response: {response.text}")
    return xmltodict.parse(response.content)


def consulta_cfdi_service(uuid: str, rfc_emisor: str, rfc_receptor: str, total_facturado: float) -> SATConsultaResponse:
    """
    Gets the status of the given CFDI by calling SAT's web service.

    Parameters
    ----------
    uuid
    rfc_emisor
    rfc_receptor
    total_facturado

    Returns
    -------
    SATConsultaResponse
    """
    data = _call_sat(uuid, rfc_emisor, rfc_receptor, total_facturado)
    try:
        result = data["s:Envelope"]["s:Body"]["ConsultaResponse"]["ConsultaResult"]
        return SATConsultaResponse(
            result["a:CodigoEstatus"],
            result["a:EsCancelable"],
            result["a:Estado"],
            result["a:EstatusCancelacion"],
            result["a:ValidacionEFOS"],
        )
    except KeyError:
        raise ValueError(f"The response from SAT was not in a known format. Response: {data}")
