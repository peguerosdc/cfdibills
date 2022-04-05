def get_uuid(cfdi: dict) -> str:
    """
    Gets the UUID (folio fiscal) from a CFDI
    """
    complementos = cfdi.get("complemento", [])
    complementos = complementos if isinstance(complementos, list) else [complementos]
    for complement in complementos:
        timbres = complement.get("timbre_fiscal_digital", [])
        timbres = timbres if isinstance(timbres, list) else [timbres]
        for timbre in timbres:
            if "uuid" in timbre:
                return timbre["uuid"]
    return None

def get_fecha_certificacion(cfdi: dict) -> str:
    """
    Gets fecha de certificacion from a CFDI
    """
    complementos = cfdi.get("complemento", [])
    complementos = complementos if isinstance(complementos, list) else [complementos]
    for complement in complementos:
        timbres = complement.get("timbre_fiscal_digital", [])
        timbres = timbres if isinstance(timbres, list) else [timbres]
        for timbre in timbres:
            if "fecha_timbrado" in timbre:
                return timbre["fecha_timbrado"]
    return None

def get_pac_certificado(cfdi: dict) -> str:
    """
    Gets the PAC that verified from a CFDI
    """
    complementos = cfdi.get("complemento", [])
    complementos = complementos if isinstance(complementos, list) else [complementos]
    for complement in complementos:
        timbres = complement.get("timbre_fiscal_digital", [])
        timbres = timbres if isinstance(timbres, list) else [timbres]
        for timbre in timbres:
            if "rfc_prov_certif" in timbre:
                return timbre["rfc_prov_certif"]
    return None

def get_total_iva(cfdi: dict) -> float:
    """
    Calculate the total IVA payed in the given cfdi
    """
    taxes = cfdi.get("impuestos", dict()).get("traslados", dict()).get("traslado", [])
    taxes = taxes if isinstance(taxes, list) else [taxes]
    iva = 0
    for tax in taxes:
        if tax["impuesto"] == "002":
            iva += float(tax["importe"])
    return iva

def get_total_ieps(cfdi: dict) -> float:
    """
    Calculate the total IEPS payed in the given cfdi
    """
    taxes = cfdi.get("impuestos", dict()).get("traslados", dict()).get("traslado", [])
    taxes = taxes if isinstance(taxes, list) else [taxes]
    ieps = 0
    for tax in taxes:
        if tax["impuesto"] == "003":
            ieps += float(tax["importe"])
    return ieps
