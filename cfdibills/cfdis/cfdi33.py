from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, validator


def validate_length(value: str, min_length: int, max_length: int):
    length = len(value)
    if not (min_length <= length < max_length):
        raise ValueError(f"{length=} but {min_length=} and {max_length=}")


def dict2list(original: Dict) -> List:
    if isinstance(original, dict):
        result = []
        for key in original.keys():
            temp = original[key]
            if isinstance(temp, dict):
                result += [{**temp, "tipo": key}]
            elif isinstance(temp, list):
                result += [{**t, "tipo": key} for t in temp]
    else:
        result = original
    return result


class UsoCFDI(str, Enum):
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


class Emisor(BaseModel):
    #: Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes correspondiente al
    #: contribuyente emisor del comprobante.
    rfc: str
    #: Atributo opcional para registrar el nombre, denominación o razón social del contribuyente emisor del comprobante
    nombre: Optional[str]
    #: Atributo requerido para incorporar la clave del régimen del contribuyente emisor al que aplicará el efecto
    #: fiscal de este comprobante.
    regimen_fiscal: str


class Receptor(BaseModel):
    #: Atributo requerido para precisar la Clave del Registro Federal de Contribuyentes correspondiente al
    #: contribuyente receptor del comprobante.<
    rfc: str
    #: Atributo opcional para precisar el nombre, denominación o razón social del contribuyente receptor del
    #: comprobante.
    nombre: Optional[str]
    #: Atributo condicional para registrar la clave del país de residencia para efectos fiscales del receptor del
    #: comprobante, cuando se trate de un extranjero, y que es conforme con la especificación ISO 3166-1 alpha-3.
    #: Es requerido cuando se incluya el complemento de comercio exterior o se registre el atributo NumRegIdTrib.
    residencia_fiscal: Optional[Pais]
    #: Atributo condicional para expresar el número de registro de identidad fiscal del receptor cuando sea residente
    #: en el extranjero. Es requerido cuando se incluya el complemento de comercio exterior.
    num_reg_id_trib: Optional[str]
    #: Atributo requerido para expresar la clave del uso que dará a esta factura el receptor del CFDI.
    uso_cfdi: UsoCFDI

    @validator("num_reg_id_trib")
    def condiciones_de_pago_must_be_valid(cls, condiciones_de_pago: str):
        validate_length(condiciones_de_pago, 1, 40)
        return condiciones_de_pago


class Impuesto(str, Enum):
    #: Impuesto Sobre la Renta (ISR)
    isr = "001"
    #: Impuesto al Valor Agregado (IVA)
    iva = "002"
    #: Impuesto Especial Sobre Producción y Servicios (IEPS)
    ieps = "003"


class TipoFactor(str, Enum):
    #: Tasa
    tasa = "Tasa"
    #: Cuota
    cuota = "Cuota"
    #: Exento
    exento = "Exento"


class Traslado(BaseModel):
    #: Atributo requerido para señalar la base para el cálculo del impuesto, la determinación de la base se realiza de
    #: acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    base: float
    #: Atributo requerido para señalar la clave del tipo de impuesto trasladado aplicable al concepto.
    impuesto: Impuesto
    #: Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    tipo_factor: TipoFactor
    #: Atributo condicional para señalar el valor de la tasa o cuota del impuesto que se traslada para el presente
    #: concepto. Es requerido cuando el atributo TipoFactor tenga una clave que corresponda a Tasa o Cuota.
    tasa_o_cuota: Optional[float]
    #: Atributo condicional para señalar el importe del impuesto trasladado que aplica al concepto. No se permiten
    #: valores negativos. Es requerido cuando TipoFactor sea Tasa o Cuota
    importe: Optional[float]


class Retencion(BaseModel):
    #: Atributo requerido para señalar la base para el cálculo del impuesto, la determinación de la base se realiza de
    #: acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    base: float
    #: Atributo requerido para señalar la clave del tipo de impuesto retenido aplicable al concepto.
    impuesto: Impuesto
    #: Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    tipo_factor: TipoFactor
    #: Atributo condicional para señalar el valor de la tasa o cuota del impuesto que se retiene para el presente
    #: concepto. Es requerido cuando el atributo TipoFactor tenga una clave que corresponda a Tasa o Cuota.
    tasa_o_cuota: float
    #: Atributo requerido para señalar el importe del impuesto retenido que aplica al concepto.
    #: No se permiten valores negativos.
    importe: float


class ImpuestosConcepto(BaseModel):
    #: Nodo opcional para asentar los impuestos trasladados aplicables al presente concepto.
    traslados: List[Traslado] = []
    #: Nodo opcional para asentar los impuestos retenidos aplicables al presente concepto.
    retenciones: List[Retencion] = []

    @validator("traslados", pre=True)
    def traslados_is_array(cls, traslados):
        return dict2list(traslados)

    @validator("retenciones", pre=True)
    def retenciones_is_array(cls, retenciones):
        return dict2list(retenciones)


class InformacionAduanera(BaseModel):
    #: Atributo requerido para expresar el número del pedimento que ampara la importación del bien que se expresa en el
    #: siguiente formato: últimos 2 dígitos del año de validación seguidos por dos espacios, 2 dígitos de la aduana de
    #: despacho seguidos por dos espacios, 4 dígitos del número de la patente seguidos por dos espacios, 1 dígito que
    #: corresponde al último dígito del año en curso, salvo que se trate de un pedimento consolidado iniciado en el año
    #: inmediato anterior o del pedimento original de una rectificación, seguido de 6 dígitos de la numeración
    #: progresiva por aduana.
    numero_pedimento: str


class CuentaPredial(BaseModel):
    #: Atributo requerido para precisar el número de la cuenta predial del inmueble cubierto por el presente concepto,
    #: o bien para incorporar los datos de identificación del certificado de participación inmobiliaria no amortizable,
    #: tratándose de arrendamiento.
    numero: str


class Parte(BaseModel):
    #: Nodo opcional para introducir la información aduanera aplicable cuando se trate de ventas de primera mano de
    #: mercancías importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    informacion_aduanera: List[InformacionAduanera] = []
    #: Atributo requerido para expresar la clave del producto o del servicio amparado por la presente parte.
    #: Es requerido y deben utilizar las claves del catálogo de productos y servicios, cuando los conceptos que
    #: registren por sus actividades correspondan con dichos conceptos.
    clave_prod_serv: str
    #: Atributo opcional para expresar el número de serie, número de parte del bien o identificador del producto o del
    #: servicio amparado por la presente parte. Opcionalmente se puede utilizar claves del estándar GTIN
    no_identificacion: Optional[str]
    #: Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por la presente
    #: parte.
    cantidad: float
    #: Atributo opcional para precisar la unidad de medida propia de la operación del emisor, aplicable para la
    #: cantidad expresada en la parte. La unidad debe corresponder con la descripción de la parte.
    unidad: Optional[str]
    #: Atributo requerido para precisar la descripción del bien o servicio cubierto por la presente parte.
    descripcion: str
    #: Atributo opcional para precisar el valor o precio unitario del bien o servicio cubierto por la presente parte.
    #: No se permiten valores negativos
    valor_unitario: Optional[float]
    #: Atributo opcional para precisar el importe total de los bienes o servicios de la presente parte. Debe ser
    #: equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en la parte.
    #: No se permiten valores negativos.
    importe: Optional[float]


class Concepto(BaseModel):
    #: Nodo opcional para capturar los impuestos aplicables al presente concepto. Cuando un concepto no registra un
    #: impuesto, implica que no es objeto del mismo.
    impuestos: Optional[ImpuestosConcepto]
    #: Nodo opcional para introducir la información aduanera aplicable cuando se trate de ventas de primera mano de
    #: mercancías importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    informacion_aduanera: List[InformacionAduanera] = []
    #: Nodo opcional para asentar el número de cuenta predial con el que fue registrado el inmueble, en el sistema
    #: catastral de la entidad federativa de que trate, o bien para incorporar los datos de identificación del
    #: certificado de participación inmobiliaria no amortizable.
    cuenta_predial: List[CuentaPredial] = []
    #: Nodo opcional donde se incluyen los nodos complementarios de extensión al concepto definidos por el SAT,
    #: de acuerdo con las disposiciones particulares para un sector o actividad específica.
    # TODO: agrega timbre fiscal digital
    complemento_concepto: List[Dict] = []
    #: Nodo opcional para expresar las partes o componentes que integran la totalidad del concepto expresado en el
    #: comprobante fiscal digital por Internet.
    parte: List[Parte] = []
    #: Atributo requerido para expresar la clave del producto o del servicio amparado por el presente concepto.
    #: Es requerido y deben utilizar las claves del catálogo de productos y servicios, cuando los conceptos que
    #: registren por sus actividades correspondan con dichos conceptos.
    clave_prod_serv: str
    #: Atributo opcional para expresar el número de parte, identificador del producto o del servicio, la clave de
    #: producto o servicio, SKU o equivalente, propia de la operación del emisor, amparado por el presente concepto.
    #: Opcionalmente se puede utilizar claves del estándar GTIN.
    no_identificacion: Optional[str]
    #: Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por el presente
    #: concepto.
    cantidad: float
    #: Atributo requerido para precisar la clave de unidad de medida estandarizada aplicable para la cantidad expresada
    #: en el concepto. La unidad debe corresponder con la descripción del concepto.
    clave_unidad: str
    #: Atributo opcional para precisar la unidad de medida propia de la operación del emisor, aplicable para la
    #: cantidad expresada en el concepto. La unidad debe corresponder con la descripción del concepto.
    unidad: Optional[str]
    #: Atributo requerido para precisar la descripción del bien o servicio cubierto por el presente concepto.
    descripcion: str
    #: Atributo requerido para precisar el valor o precio unitario del bien o servicio cubierto por el presente concepto
    valor_unitario: float
    #: Atributo requerido para precisar el importe total de los bienes o servicios del presente concepto. Debe ser
    #: equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en el concepto.
    #: No se permiten valores negativos.
    importe: float
    #: Atributo opcional para representar el importe de los descuentos aplicables al concepto. No se permiten valores
    #: negativos.
    descuento: Optional[float]

    @validator("complemento_concepto", pre=True)
    def complemento_concepto_is_array(cls, complemento_concepto):
        return dict2list(complemento_concepto)


class RetencionCFDI(BaseModel):
    #: Atributo requerido para señalar la clave del tipo de impuesto retenido
    impuesto: Impuesto
    #: Atributo requerido para señalar el monto del impuesto retenido. No se permiten valores negativos.
    importe: float


class TrasladoCFDI(BaseModel):
    #: Atributo requerido para señalar la clave del tipo de impuesto trasladado.
    impuesto: Impuesto
    #: Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    tipo_factor: TipoFactor
    #: Atributo requerido para señalar el valor de la tasa o cuota del impuesto que se traslada por los conceptos
    #: amparados en el comprobante.
    tasa_o_cuota: float
    #: Atributo requerido para señalar la suma del importe del impuesto trasladado, agrupado por impuesto, TipoFactor
    #: y TasaOCuota. No se permiten valores negativos.
    importe: float


class ImpuestosCFDI(BaseModel):
    #: Nodo condicional para capturar los impuestos retenidos aplicables. Es requerido cuando en los conceptos se
    #: registre algún impuesto retenido
    retenciones: List[RetencionCFDI] = []
    #: Nodo condicional para capturar los impuestos trasladados aplicables. Es requerido cuando en los conceptos se
    #: registre un impuesto trasladado.
    traslados: List[TrasladoCFDI] = []
    #: Atributo condicional para expresar el total de los impuestos retenidos que se desprenden de los conceptos
    #: expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando
    #: en los conceptos se registren impuestos retenidos
    total_impuestos_retenidos: float = 0.0
    #: Atributo condicional para expresar el total de los impuestos trasladados que se desprenden de los conceptos
    #: expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando
    #: en los conceptos se registren impuestos trasladados.
    total_impuestos_trasladados: float = 0.0

    @validator("traslados", pre=True)
    def traslados_is_array(cls, traslados):
        return dict2list(traslados)

    @validator("retenciones", pre=True)
    def retenciones_is_array(cls, retenciones):
        return dict2list(retenciones)


class TimbreFiscalDigital(BaseModel):
    """
    http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/cfd/timbrefiscaldigital/TimbreFiscalDigitalv11.xsd
    """

    version: str
    uuid: UUID
    fecha_timbrado: datetime
    rfc_prov_certif: str
    sello_cfd: str
    no_certificado_sat: str
    sello_sat: str

    @validator("fecha_timbrado", pre=True)
    def parse_fecha(cls, fecha_timbrado: str):
        return datetime.strptime(fecha_timbrado, "%Y-%m-%dT%H:%M:%S")


class Complemento(BaseModel):
    timbre_fiscal_digital: TimbreFiscalDigital


class CfdiRelacionado(BaseModel):
    #: Atributo requerido para registrar el folio fiscal (UUID) de un CFDI relacionado con el presente comprobante,
    #: por ejemplo: Si el CFDI relacionado es un comprobante de traslado que sirve para registrar el movimiento de la
    #: mercancía. Si este comprobante se usa como nota de crédito o nota de débito del comprobante relacionado.
    #: Si este comprobante es una devolución sobre el comprobante relacionado. Si éste sustituye a una factura
    #: cancelada.
    uuid: UUID
    #: Atributo requerido para indicar la clave de la relación que existe entre éste que se esta generando y el o
    #: los CFDI previos.
    tipo_relacion: TipoRelacion


class TipoDeComprobante(str, Enum):
    ingreso = "I"
    egreso = "E"
    traslado = "T"
    nomina = "N"
    pago = "P"


class MetodoDePago(str, Enum):
    #: Pago en una sola exhibición
    pue = "PUE"
    #: Pago en parcialidades o diferido
    ppd = "PPD"


class FormaPago(str, Enum):
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


class CFDI33(BaseModel):
    #: Atributo requerido con valor prefijado a 3.3 que indica la versión del estándar bajo el que se encuentra
    #: expresado el comprobante.
    version: str
    #: Atributo opcional para precisar la serie para control interno del contribuyente. Este atributo acepta
    #: una cadena de caracteres
    serie: Optional[str]
    #: Atributo opcional para control interno del contribuyente que expresa el folio del comprobante, acepta una
    #: cadena de caracteres.
    folio: Optional[str]
    #: Atributo requerido para la expresión de la fecha y hora de expedición del Comprobante Fiscal Digital por
    #: Internet. Se expresa en la forma AAAA-MM-DDThh:mm:ss y debe corresponder con la hora local donde se expide el
    #: comprobante.
    fecha: datetime
    #: Atributo requerido para contener el sello digital del comprobante fiscal, al que hacen referencia las reglas
    #: de resolución miscelánea vigente. El sello debe ser expresado como una cadena de texto en formato Base 64.
    sello: str
    #: Atributo condicional para expresar la clave de la forma de pago de los bienes o servicios amparados por el
    #: comprobante. Si no se conoce la forma de pago este atributo se debe omitir.
    forma_pago: Optional[FormaPago]
    #: Atributo requerido para expresar el número de serie del certificado de sello digital que ampara al comprobante,
    #: de acuerdo con el acuse correspondiente a 20 posiciones otorgado por el sistema del SAT.
    no_certificado: str
    #: Atributo requerido que sirve para incorporar el certificado de sello digital que ampara al comprobante, como
    #: texto en formato base 64.
    certificado: str
    #: Atributo condicional para expresar las condiciones comerciales aplicables para el pago del comprobante fiscal
    #: digital por Internet. Este atributo puede ser condicionado mediante atributos o complementos.
    condiciones_de_pago: Optional[str]
    #: Atributo requerido para representar la suma de los importes de los conceptos antes de descuentos e impuesto.
    #: No se permiten valores negativos.
    sub_total: float
    #: Atributo condicional para representar el importe total de los descuentos aplicables antes de impuestos. No se
    #: permiten valores negativos. Se debe registrar cuando existan conceptos con descuento.
    descuento: float = 0.0
    #: Atributo requerido para identificar la clave de la moneda utilizada para expresar los montos, cuando se usa
    #: moneda nacional se registra MXN. Conforme con la especificación ISO 4217.
    moneda: Moneda
    #: Atributo condicional para representar el tipo de cambio conforme con la moneda usada. Es requerido cuando la
    #: clave de moneda es distinta de MXN y de XXX. El valor debe reflejar el número de pesos mexicanos que equivalen
    #: a una unidad de la divisa señalada en el atributo moneda. Si el valor está fuera del porcentaje aplicable a la
    #: moneda tomado del catálogo c_Moneda, el emisor debe obtener del PAC que vaya a timbrar el CFDI, de manera no
    #: automática, una clave de confirmación para ratificar que el valor es correcto e integrar dicha clave en el
    #: atributo Confirmacion.
    tipo_cambio: Optional[float]
    #: Atributo requerido para representar la suma del subtotal, menos los descuentos aplicables, más las contribuciones
    #: recibidas (impuestos trasladados - federales o locales, derechos, productos, aprovechamientos, aportaciones de
    #: seguridad social, contribuciones de mejoras) menos los impuestos retenidos. Si el valor es superior al límite que
    #: establezca el SAT en la Resolución Miscelánea Fiscal vigente, el emisor debe obtener del PAC que vaya a timbrar
    #: el CFDI, de manera no automática, una clave de confirmación para ratificar que el valor es correcto e integrar
    #: dicha clave en el atributo Confirmacion. No se permiten valores negativos.
    total: float
    #: Atributo requerido para expresar la clave del efecto del comprobante fiscal para el contribuyente emisor.
    tipo_de_comprobante: TipoDeComprobante
    #: Atributo condicional para precisar la clave del método de pago que aplica para este comprobante fiscal digital
    #: por Internet, conforme al Artículo 29-A fracción VII incisos a y b del CFF
    metodo_pago: Optional[MetodoDePago]
    #: Atributo requerido para incorporar el código postal del lugar de expedición del comprobante (domicilio de la
    #: matriz o de la sucursal).
    lugar_expedicion: str
    #: Atributo condicional para registrar la clave de confirmación que entregue el PAC para expedir el comprobante con
    #: importes grandes, con un tipo de cambio fuera del rango establecido o con ambos casos. Es requerido cuando se
    #: registra un tipo de cambio o un total fuera del rango establecido.
    confirmacion: Optional[str]
    #: Nodo opcional para precisar la información de los comprobantes relacionados.
    cfdi_relacionados: Optional[List[CfdiRelacionado]]
    #: Nodo requerido para expresar la información del contribuyente emisor del comprobante.
    emisor: Emisor
    #: Nodo requerido para precisar la información del contribuyente receptor del comprobante
    receptor: Receptor
    #: Nodo requerido para listar los conceptos cubiertos por el comprobante.
    conceptos: List[Concepto]
    #: Nodo condicional para expresar el resumen de los impuestos aplicables.
    impuestos: ImpuestosCFDI
    #: Nodo opcional donde se incluye el complemento Timbre Fiscal Digital de manera obligatoria y los nodos
    #: complementarios determinados por el SAT, de acuerdo con las disposiciones particulares para un sector o
    #: actividad específica.
    complemento: Optional[List[Union[TimbreFiscalDigital, Dict]]]
    #: Nodo opcional para recibir las extensiones al presente formato que sean de utilidad al contribuyente.
    #: Para las reglas de uso del mismo, referirse al formato origen.
    addenda: Optional[Dict]

    @validator("complemento", pre=True)
    def complemento_is_array(cls, complemento):
        return dict2list(complemento)

    @validator("conceptos", pre=True)
    def conceptos_is_array(cls, conceptos):
        return dict2list(conceptos)

    @validator("version")
    def version_must_be_33(cls, v: str):
        if v != "3.3":
            raise ValueError(f"Version must be fixed to '3.3'")
        return v

    @validator("serie")
    def serie_must_be_valid(cls, serie: str):
        validate_length(serie, 1, 25)
        return serie

    @validator("folio")
    def folio_must_be_valid(cls, folio: str):
        validate_length(folio, 1, 40)
        return folio

    @validator("fecha", pre=True)
    def parse_fecha(cls, fecha: str):
        return datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")

    @validator("no_certificado")
    def no_certificado_must_be_valid(cls, no_certificado: str):
        if not no_certificado.isnumeric() or len(no_certificado) != 20:
            raise ValueError(f"{no_certificado=} must be numeric of length 20")
        return no_certificado

    @validator("condiciones_de_pago")
    def condiciones_de_pago_must_be_valid(cls, condiciones_de_pago: str):
        validate_length(condiciones_de_pago, 1, 1000)
        return condiciones_de_pago

    @validator("sub_total")
    def sub_total_must_be_positive(cls, sub_total: float):
        if sub_total < 0:
            raise ValueError(f"{sub_total=} must be a positive number")
        return sub_total

    @validator("descuento")
    def descuento_must_be_positive(cls, descuento: float):
        if descuento < 0:
            raise ValueError(f"{descuento=} must be a positive number")
        return descuento

    @validator("confirmacion")
    def confirmacion_must_be_valid(cls, confirmacion: str):
        length = len(confirmacion)
        if length != 5:
            raise ValueError(f"{confirmacion=} must be of length=5")
        return confirmacion

    def get_total_iva(self) -> float:
        total = 0
        traslados = self.impuestos.traslados
        for traslado in traslados:
            if traslado.impuesto == Impuesto.iva:
                total += traslado.importe
        return total

    def get_total_ieps(self) -> float:
        total = 0
        traslados = self.impuestos.traslados
        for traslado in traslados:
            if traslado.impuesto == Impuesto.ieps:
                total += traslado.importe
        return total

    def get_timbre_fiscal_digital(self) -> TimbreFiscalDigital:
        for complemento in self.complemento:
            if isinstance(complemento, TimbreFiscalDigital):
                return complemento
        raise ValueError("This CFDI is not certified")


"""
http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd
http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
"""
