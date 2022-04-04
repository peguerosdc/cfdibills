def get_uuid(cfdi: dict) -> str:
    """
    Gets the UUID (folio fiscal) from a CFDI
    """
    for complement in cfdi["complemento"]:
        timbres = complement.get("timbre_fiscal_digital", [])
        for timbre in timbres:
            if "uuid" in timbre:
                return timbre["uuid"]
    return None

def get_fecha_certificacion(cfdi: dict) -> str:
    """
    Gets fecha de certificacion from a CFDI
    """
    for complement in cfdi["complemento"]:
        timbres = complement.get("timbre_fiscal_digital", [])
        for timbre in timbres:
            if "fecha_timbrado" in timbre:
                return timbre["fecha_timbrado"]
    return None

def get_pac_certificado(cfdi: dict) -> str:
    """
    Gets the PAC that verified from a CFDI
    """
    for complement in cfdi["complemento"]:
        timbres = complement.get("timbre_fiscal_digital", [])
        for timbre in timbres:
            if "rfc_prov_certif" in timbre:
                return timbre["rfc_prov_certif"]
    return None

def get_total_iva(cfdi: dict) -> float:
    """
    Calculate the total IVA payed in the given cfdi
    """
    taxes = cfdi.get("impuestos", dict()).get("traslados", dict()).get("traslado", [])
    iva = 0
    for tax in taxes:
        if tax["impuesto"] == "002":
            iva += tax["importe"]
    return iva

def get_total_ieps(cfdi: dict) -> float:
    """
    Calculate the total IEPS payed in the given cfdi
    """
    taxes = cfdi.get("impuestos", dict()).get("traslados", dict()).get("traslado", [])
    ieps = 0
    for tax in taxes:
        if tax["impuesto"] == "003":
            ieps += tax["importe"]
    return ieps
