"""
Catalogs required to define CFDIs.
"""

from enum import Enum


class UsoCFDI(str, Enum):
    """
    Catalog of "Uso CFDI".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Adquisición de mercancías
    G01 = "G01"
    #: Devoluciones, descuentos o bonificaciones
    G02 = "G02"
    #: Gastos en general
    G03 = "G03"
    #: Construcciones
    I01 = "I01"
    #: Mobiliario y equipo de oficina por inversiones
    I02 = "I02"
    #: Equipo de transporte
    I03 = "I03"
    #: Equipo de cómputo y accesorios
    I04 = "I04"
    #: Dados, troqueles, moldes, matrices y herramental
    I05 = "I05"
    #: Comunicaciones telefónicas
    I06 = "I06"
    #: Comunicaciones satelitales
    I07 = "I07"
    #: Otra maquinaria y equipo
    I08 = "I08"
    #: Honorarios médicos, dentales y gastos hospitalarios.
    D01 = "D01"
    #: Gastos médicos por incapacidad o discapacidad
    D02 = "D02"
    #: Gastos funerales.
    D03 = "D03"
    #: Donativos.
    D04 = "D04"
    #: Intereses reales efectivamente pagados por créditos hipotecarios (casa habitación).
    D05 = "D05"
    #: Aportaciones voluntarias al SAR.
    D06 = "D06"
    #: Primas por seguros de gastos médicos.
    D07 = "D07"
    #: Gastos de transportación escolar obligatoria.
    D08 = "D08"
    #: Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones.
    D09 = "D09"
    #: Pagos por servicios educativos (colegiaturas)
    D10 = "D10"
    #: Por definir
    P01 = "P01"
    #: Sin efectos fiscales
    S01 = "S01"
    #: Pagos
    CP01 = "CP01"
    #: Nómina
    CN01 = "CN01"


class Pais(str, Enum):
    """
    Catalog of "Pais".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    AFG = "AFG"
    ALA = "ALA"
    ALB = "ALB"
    DEU = "DEU"
    AND = "AND"
    AGO = "AGO"
    AIA = "AIA"
    ATA = "ATA"
    ATG = "ATG"
    SAU = "SAU"
    DZA = "DZA"
    ARG = "ARG"
    ARM = "ARM"
    ABW = "ABW"
    AUS = "AUS"
    AUT = "AUT"
    AZE = "AZE"
    BHS = "BHS"
    BGD = "BGD"
    BRB = "BRB"
    BHR = "BHR"
    BEL = "BEL"
    BLZ = "BLZ"
    BEN = "BEN"
    BMU = "BMU"
    BLR = "BLR"
    MMR = "MMR"
    BOL = "BOL"
    BIH = "BIH"
    BWA = "BWA"
    BRA = "BRA"
    BRN = "BRN"
    BGR = "BGR"
    BFA = "BFA"
    BDI = "BDI"
    BTN = "BTN"
    CPV = "CPV"
    KHM = "KHM"
    CMR = "CMR"
    CAN = "CAN"
    QAT = "QAT"
    BES = "BES"
    TCD = "TCD"
    CHL = "CHL"
    CHN = "CHN"
    CYP = "CYP"
    COL = "COL"
    COM = "COM"
    PRK = "PRK"
    KOR = "KOR"
    CIV = "CIV"
    CRI = "CRI"
    HRV = "HRV"
    CUB = "CUB"
    CUW = "CUW"
    DNK = "DNK"
    DMA = "DMA"
    ECU = "ECU"
    EGY = "EGY"
    SLV = "SLV"
    ARE = "ARE"
    ERI = "ERI"
    SVK = "SVK"
    SVN = "SVN"
    ESP = "ESP"
    USA = "USA"
    EST = "EST"
    ETH = "ETH"
    PHL = "PHL"
    FIN = "FIN"
    FJI = "FJI"
    FRA = "FRA"
    GAB = "GAB"
    GMB = "GMB"
    GEO = "GEO"
    GHA = "GHA"
    GIB = "GIB"
    GRD = "GRD"
    GRC = "GRC"
    GRL = "GRL"
    GLP = "GLP"
    GUM = "GUM"
    GTM = "GTM"
    GUF = "GUF"
    GGY = "GGY"
    GIN = "GIN"
    GNB = "GNB"
    GNQ = "GNQ"
    GUY = "GUY"
    HTI = "HTI"
    HND = "HND"
    HKG = "HKG"
    HUN = "HUN"
    IND = "IND"
    IDN = "IDN"
    IRQ = "IRQ"
    IRN = "IRN"
    IRL = "IRL"
    BVT = "BVT"
    IMN = "IMN"
    CXR = "CXR"
    NFK = "NFK"
    ISL = "ISL"
    CYM = "CYM"
    CCK = "CCK"
    COK = "COK"
    FRO = "FRO"
    SGS = "SGS"
    HMD = "HMD"
    FLK = "FLK"
    MNP = "MNP"
    MHL = "MHL"
    PCN = "PCN"
    SLB = "SLB"
    TCA = "TCA"
    UMI = "UMI"
    VGB = "VGB"
    VIR = "VIR"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JPN = "JPN"
    JEY = "JEY"
    JOR = "JOR"
    KAZ = "KAZ"
    KEN = "KEN"
    KGZ = "KGZ"
    KIR = "KIR"
    KWT = "KWT"
    LAO = "LAO"
    LSO = "LSO"
    LVA = "LVA"
    LBN = "LBN"
    LBR = "LBR"
    LBY = "LBY"
    LIE = "LIE"
    LTU = "LTU"
    LUX = "LUX"
    MAC = "MAC"
    MDG = "MDG"
    MYS = "MYS"
    MWI = "MWI"
    MDV = "MDV"
    MLI = "MLI"
    MLT = "MLT"
    MAR = "MAR"
    MTQ = "MTQ"
    MUS = "MUS"
    MRT = "MRT"
    MYT = "MYT"
    MEX = "MEX"
    FSM = "FSM"
    MDA = "MDA"
    MCO = "MCO"
    MNG = "MNG"
    MNE = "MNE"
    MSR = "MSR"
    MOZ = "MOZ"
    NAM = "NAM"
    NRU = "NRU"
    NPL = "NPL"
    NIC = "NIC"
    NER = "NER"
    NGA = "NGA"
    NIU = "NIU"
    NOR = "NOR"
    NCL = "NCL"
    NZL = "NZL"
    OMN = "OMN"
    NLD = "NLD"
    PAK = "PAK"
    PLW = "PLW"
    PSE = "PSE"
    PAN = "PAN"
    PNG = "PNG"
    PRY = "PRY"
    PER = "PER"
    PYF = "PYF"
    POL = "POL"
    PRT = "PRT"
    PRI = "PRI"
    GBR = "GBR"
    CAF = "CAF"
    CZE = "CZE"
    MKD = "MKD"
    COG = "COG"
    COD = "COD"
    DOM = "DOM"
    REU = "REU"
    RWA = "RWA"
    ROU = "ROU"
    RUS = "RUS"
    ESH = "ESH"
    WSM = "WSM"
    ASM = "ASM"
    BLM = "BLM"
    KNA = "KNA"
    SMR = "SMR"
    MAF = "MAF"
    SPM = "SPM"
    VCT = "VCT"
    SHN = "SHN"
    LCA = "LCA"
    STP = "STP"
    SEN = "SEN"
    SRB = "SRB"
    SYC = "SYC"
    SLE = "SLE"
    SGP = "SGP"
    SXM = "SXM"
    SYR = "SYR"
    SOM = "SOM"
    LKA = "LKA"
    SWZ = "SWZ"
    ZAF = "ZAF"
    SDN = "SDN"
    SSD = "SSD"
    SWE = "SWE"
    CHE = "CHE"
    SUR = "SUR"
    SJM = "SJM"
    THA = "THA"
    TWN = "TWN"
    TZA = "TZA"
    TJK = "TJK"
    IOT = "IOT"
    ATF = "ATF"
    TLS = "TLS"
    TGO = "TGO"
    TKL = "TKL"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TKM = "TKM"
    TUR = "TUR"
    TUV = "TUV"
    UKR = "UKR"
    UGA = "UGA"
    URY = "URY"
    UZB = "UZB"
    VUT = "VUT"
    VAT = "VAT"
    VEN = "VEN"
    VNM = "VNM"
    WLF = "WLF"
    YEM = "YEM"
    DJI = "DJI"
    ZMB = "ZMB"
    ZWE = "ZWE"
    ZZZ = "ZZZ"


class Impuesto(str, Enum):
    """
    Catalog of "Impuesto".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Impuesto Sobre la Renta (ISR)
    isr = "001"
    #: Impuesto al Valor Agregado (IVA)
    iva = "002"
    #: Impuesto Especial Sobre Producción y Servicios (IEPS)
    ieps = "003"


class TipoFactor(str, Enum):
    """
    Catalog of "Tipo Factor".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Tasa
    tasa = "Tasa"
    #: Cuota
    cuota = "Cuota"
    #: Exento
    exento = "Exento"


class TipoDeComprobante(str, Enum):
    """
    Catalog of "Tipo De Comprobante".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Ingreso
    ingreso = "I"
    #: Egreso
    egreso = "E"
    #: Traslado
    traslado = "T"
    #: Nomina
    nomina = "N"
    #: Pago
    pago = "P"


class MetodoDePago(str, Enum):
    """
    Catalog of "Metodo De Pago".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Pago en una sola exhibición
    pue = "PUE"
    #: Pago en parcialidades o diferido
    ppd = "PPD"


class FormaPago(str, Enum):
    """
    Catalog of "Forma Pago".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Efectivo
    efectivo = "01"
    #: Cheque nominativo
    cheque_nominativo = "02"
    #: Transferencia electrónica de fondos
    transferencia = "03"
    #: Tarjeta de crédito
    tarjeta_de_credito = "04"
    #: Monedero electrónico
    monedero_electronico = "05"
    #: Dinero electrónico
    dinero_electronico = "06"
    #: Vales de despensa
    vales_de_despensa = "08"
    #: Dación en pago
    dacion_en_pago = "12"
    #: Pago por subrogación
    pago_subrogacion = "13"
    #: Pago por consignación
    pago_consignacion = "14"
    #: Condonación
    condonacion = "15"
    #: Compensación
    compensacion = "17"
    #: Novación
    novacion = "23"
    #: Confusión
    confusion = "24"
    #: Remisión de deuda
    remision = "25"
    #: Prescripción o caducidad
    prescripcion = "26"
    #: A satisfacción del acreedor
    a_satisfaccion = "27"
    #: Tarjeta de débito
    tarjeta_de_debito = "28"
    #: Tarjeta de servicios
    tarjeta_de_servicios = "29"
    #: Aplicación de anticipos
    aplicacion_de_anticipos = "30"
    #: Intermediario pagos
    intermediario_pagos = "31"
    #: Por definir
    por_definir = "99"


class Moneda(str, Enum):
    """
    Catalog of "Moneda".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    UYI = "UYI"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    XSU = "XSU"
    XTS = "XTS"
    XUA = "XUA"
    XXX = "XXX"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWL = "ZWL"


class TipoRelacion(str, Enum):
    """
    Catalog of "Tipo Relacion".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Nota de crédito de los documentos relacionados
    nota_credito = "01"
    #: Nota de débito de los documentos relacionados
    nota_debito = "02"
    #: Devolución de mercancía sobre facturas o traslados previos
    devolucion = "03"
    #: Sustitución de los CFDI previos
    sustitucion = "04"
    #: Traslados de mercancias facturados previamente
    traslados = "05"
    #: Factura generada por los traslados previos
    factura_traslados = "06"
    #: CFDI por aplicación de anticipo
    aplicacion_de_anticipo = "07"
    #: Facturas Generadas por Pagos en Parcialidades
    pagos_en_parcialidades = "08"
    #: Factura Generada por Pagos Diferidos
    pagos_diferidos = "09"


class RegimenFiscal(str, Enum):
    """
    Catalog of "Regimen Fiscal".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    r601 = "601"
    r603 = "603"
    r605 = "605"
    r606 = "606"
    r607 = "607"
    r608 = "608"
    r609 = "609"
    r610 = "610"
    r611 = "611"
    r612 = "612"
    r614 = "614"
    r615 = "615"
    r616 = "616"
    r620 = "620"
    r621 = "621"
    r622 = "622"
    r623 = "623"
    r624 = "624"
    r625 = "625"
    r626 = "626"
    r628 = "628"
    r629 = "629"
    r630 = "630"


class ObjetoImp(str, Enum):
    """
    Catalog of "Objecto Imp".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    o01 = "01"
    o02 = "02"
    o03 = "03"


class Periodicidad(str, Enum):
    """
    Catalog of "Periodicidad".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    p01 = "01"
    p02 = "02"
    p03 = "03"
    p04 = "04"
    p05 = "05"


class Meses(str, Enum):
    """
    Catalog of "Meses".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    m01 = "01"
    m02 = "02"
    m03 = "03"
    m04 = "04"
    m05 = "05"
    m06 = "06"
    m07 = "07"
    m08 = "08"
    m09 = "09"
    m10 = "10"
    m11 = "11"
    m12 = "12"
    m13 = "13"
    m14 = "14"
    m15 = "15"
    m16 = "16"
    m17 = "17"
    m18 = "18"


class Exportacion(str, Enum):
    """
    Catalog of "Exportacion".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    e01 = "01"
    e02 = "02"
    e03 = "03"
    e04 = "04"
