"""
Schemas of CFDI v3.3.
"""

from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Literal, Optional
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeFloat
from typing_extensions import Annotated

from cfdibills.schemas.catalogs import (
    FormaPago,
    Impuesto,
    MetodoDePago,
    Moneda,
    Pais,
    RegimenFiscal,
    TipoDeComprobante,
    TipoFactor,
    TipoRelacion,
    UsoCFDI,
)
from cfdibills.schemas.complementos import ComplementoType
from cfdibills.schemas.fields import RFC, NonNegativeSixDecimals, PositiveSixDecimals
from cfdibills.schemas.mixins import CFDIMixin
from cfdibills.schemas.validators import (
    dict2list,
    dict2list_flatten,
    reusable_validator,
)


class Emisor(BaseModel):
    """
    Schema of a "Emisor" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes correspondiente al
    #: contribuyente emisor del comprobante.
    rfc: RFC
    #: Atributo opcional para registrar el nombre, denominación o razón social del contribuyente emisor del comprobante
    nombre: Optional[Annotated[str, Field(regex=r"[^|]{1,254}")]]
    #: Atributo requerido para incorporar la clave del régimen del contribuyente emisor al que aplicará el efecto
    #: fiscal de este comprobante.
    regimen_fiscal: RegimenFiscal


class Receptor(BaseModel):
    """
    Schema of a "Receptor" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para precisar la Clave del Registro Federal de Contribuyentes correspondiente al
    #: contribuyente receptor del comprobante.<
    rfc: RFC
    #: Atributo opcional para precisar el nombre, denominación o razón social del contribuyente receptor del
    #: comprobante.
    nombre: Optional[str]
    #: Atributo condicional para registrar la clave del país de residencia para efectos fiscales del receptor del
    #: comprobante, cuando se trate de un extranjero, y que es conforme con la especificación ISO 3166-1 alpha-3.
    #: Es requerido cuando se incluya el complemento de comercio exterior o se registre el atributo NumRegIdTrib.
    residencia_fiscal: Optional[Pais]
    #: Atributo condicional para expresar el número de registro de identidad fiscal del receptor cuando sea residente
    #: en el extranjero. Es requerido cuando se incluya el complemento de comercio exterior.
    num_reg_id_trib: Optional[Annotated[str, Field(min_length=1, max_length=40)]]
    #: Atributo requerido para expresar la clave del uso que dará a esta factura el receptor del CFDI.
    uso_cfdi: UsoCFDI


class Traslado(BaseModel):
    """
    Schema of a "Concepto / Impuestos / Traslado" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para señalar la base para el cálculo del impuesto, la determinación de la base se realiza de
    #: acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    base: PositiveSixDecimals
    #: Atributo requerido para señalar la clave del tipo de impuesto trasladado aplicable al concepto.
    impuesto: Impuesto
    #: Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    tipo_factor: TipoFactor
    #: Atributo condicional para señalar el valor de la tasa o cuota del impuesto que se traslada para el presente
    #: concepto. Es requerido cuando el atributo TipoFactor tenga una clave que corresponda a Tasa o Cuota.
    tasa_o_cuota: Optional[NonNegativeSixDecimals]
    #: Atributo condicional para señalar el importe del impuesto trasladado que aplica al concepto. No se permiten
    #: valores negativos. Es requerido cuando TipoFactor sea Tasa o Cuota
    importe: Optional[NonNegativeSixDecimals]


class Retencion(BaseModel):
    """
    Schema of a "Concepto / Impuestos / Retencion" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para señalar la base para el cálculo del impuesto, la determinación de la base se realiza de
    #: acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    base: PositiveSixDecimals
    #: Atributo requerido para señalar la clave del tipo de impuesto retenido aplicable al concepto.
    impuesto: Impuesto
    #: Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    tipo_factor: TipoFactor
    #: Atributo condicional para señalar el valor de la tasa o cuota del impuesto que se retiene para el presente
    #: concepto. Es requerido cuando el atributo TipoFactor tenga una clave que corresponda a Tasa o Cuota.
    tasa_o_cuota: NonNegativeSixDecimals
    #: Atributo requerido para señalar el importe del impuesto retenido que aplica al concepto.
    #: No se permiten valores negativos.
    importe: NonNegativeSixDecimals


class ImpuestosConcepto(BaseModel):
    """
    Schema of a "Concepto / Impuestos" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Nodo opcional para asentar los impuestos trasladados aplicables al presente concepto.
    traslados: List[Traslado] = []
    #: Nodo opcional para asentar los impuestos retenidos aplicables al presente concepto.
    retenciones: List[Retencion] = []

    _to_array = reusable_validator("traslados", "retenciones", pre=True)(dict2list_flatten)


class InformacionAduanera(BaseModel):
    """
    Schema of a "Informacion Aduanera" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para expresar el número del pedimento que ampara la importación del bien que se expresa en el
    #: siguiente formato: últimos 2 dígitos del año de validación seguidos por dos espacios, 2 dígitos de la aduana de
    #: despacho seguidos por dos espacios, 4 dígitos del número de la patente seguidos por dos espacios, 1 dígito que
    #: corresponde al último dígito del año en curso, salvo que se trate de un pedimento consolidado iniciado en el año
    #: inmediato anterior o del pedimento original de una rectificación, seguido de 6 dígitos de la numeración
    #: progresiva por aduana.
    numero_pedimento: Annotated[
        str, Field(min_length=21, max_length=21, regex=r"[0-9]{2}  [0-9]{2}  [0-9]{4}  [0-9]{7}")
    ]


class CuentaPredial(BaseModel):
    """
    Schema of a "Cuenta Predial" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para precisar el número de la cuenta predial del inmueble cubierto por el presente concepto,
    #: o bien para incorporar los datos de identificación del certificado de participación inmobiliaria no amortizable,
    #: tratándose de arrendamiento.
    numero: Annotated[str, Field(min_length=1, max_length=150, regex=r"[0-9]{1,150}")]


class Parte(BaseModel):
    """
    Schema of a "Parte" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Nodo opcional para introducir la información aduanera aplicable cuando se trate de ventas de primera mano de
    #: mercancías importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    informacion_aduanera: List[InformacionAduanera] = []
    #: Atributo requerido para expresar la clave del producto o del servicio amparado por la presente parte.
    #: Es requerido y deben utilizar las claves del catálogo de productos y servicios, cuando los conceptos que
    #: registren por sus actividades correspondan con dichos conceptos.
    clave_prod_serv: str
    #: Atributo opcional para expresar el número de serie, número de parte del bien o identificador del producto o del
    #: servicio amparado por la presente parte. Opcionalmente se puede utilizar claves del estándar GTIN
    no_identificacion: Optional[Annotated[str, Field(min_length=1, max_length=100, regex=r"[^|]{1,100}")]]
    #: Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por la presente
    #: parte.
    cantidad: PositiveSixDecimals
    #: Atributo opcional para precisar la unidad de medida propia de la operación del emisor, aplicable para la
    #: cantidad expresada en la parte. La unidad debe corresponder con la descripción de la parte.
    unidad: Optional[Annotated[str, Field(min_length=1, max_length=20, regex=r"[^|]{1,20}")]]
    #: Atributo requerido para precisar la descripción del bien o servicio cubierto por la presente parte.
    descripcion: Annotated[str, Field(min_length=1, max_length=1000, regex=r"[^|]{1,1000}")]
    #: Atributo opcional para precisar el valor o precio unitario del bien o servicio cubierto por la presente parte.
    #: No se permiten valores negativos
    valor_unitario: Optional[NonNegativeFloat]
    #: Atributo opcional para precisar el importe total de los bienes o servicios de la presente parte. Debe ser
    #: equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en la parte.
    #: No se permiten valores negativos.
    importe: Optional[NonNegativeSixDecimals]

    _to_array = reusable_validator("informacion_aduanera", pre=True)(dict2list)


class Concepto(BaseModel):
    """
    Schema of a "Concepto" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

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
    no_identificacion: Optional[Annotated[str, Field(min_length=1, max_length=100, regex=r"[^|]{1,100}")]]
    #: Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por el presente
    #: concepto.
    cantidad: PositiveSixDecimals
    #: Atributo requerido para precisar la clave de unidad de medida estandarizada aplicable para la cantidad expresada
    #: en el concepto. La unidad debe corresponder con la descripción del concepto.
    clave_unidad: str
    #: Atributo opcional para precisar la unidad de medida propia de la operación del emisor, aplicable para la
    #: cantidad expresada en el concepto. La unidad debe corresponder con la descripción del concepto.
    unidad: Optional[Annotated[str, Field(min_length=1, max_length=20, regex=r"[^|]{1,20}")]]
    #: Atributo requerido para precisar la descripción del bien o servicio cubierto por el presente concepto.
    descripcion: Annotated[str, Field(min_length=1, max_length=1000, regex=r"[^|]{1,1000}")]
    #: Atributo requerido para precisar el valor o precio unitario del bien o servicio cubierto por el presente concepto
    valor_unitario: float
    #: Atributo requerido para precisar el importe total de los bienes o servicios del presente concepto. Debe ser
    #: equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en el concepto.
    #: No se permiten valores negativos.
    importe: NonNegativeSixDecimals
    #: Atributo opcional para representar el importe de los descuentos aplicables al concepto. No se permiten valores
    #: negativos.
    descuento: NonNegativeSixDecimals = Decimal(0)

    _complemento_to_array = reusable_validator(
        "complemento_concepto", "cuenta_predial", "informacion_aduanera", "parte", pre=True
    )(dict2list)


class RetencionCFDI(BaseModel):
    """
    Schema of a "Comprobante / Retencion" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para señalar la clave del tipo de impuesto retenido
    impuesto: Impuesto
    #: Atributo requerido para señalar el monto del impuesto retenido. No se permiten valores negativos.
    importe: NonNegativeSixDecimals


class TrasladoCFDI(BaseModel):
    """
    Schema of a "Comprobante / Traslado" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para señalar la clave del tipo de impuesto trasladado.
    impuesto: Impuesto
    #: Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    tipo_factor: TipoFactor
    #: Atributo requerido para señalar el valor de la tasa o cuota del impuesto que se traslada por los conceptos
    #: amparados en el comprobante.
    tasa_o_cuota: NonNegativeSixDecimals
    #: Atributo requerido para señalar la suma del importe del impuesto trasladado, agrupado por impuesto, TipoFactor
    #: y TasaOCuota. No se permiten valores negativos.
    importe: NonNegativeSixDecimals


class ImpuestosCFDI(BaseModel):
    """
    Schema of a "Comprobante / Impuestos" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Nodo condicional para capturar los impuestos retenidos aplicables. Es requerido cuando en los conceptos se
    #: registre algún impuesto retenido
    retenciones: List[RetencionCFDI] = []
    #: Nodo condicional para capturar los impuestos trasladados aplicables. Es requerido cuando en los conceptos se
    #: registre un impuesto trasladado.
    traslados: List[TrasladoCFDI] = []
    #: Atributo condicional para expresar el total de los impuestos retenidos que se desprenden de los conceptos
    #: expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando
    #: en los conceptos se registren impuestos retenidos
    total_impuestos_retenidos: NonNegativeSixDecimals = Decimal(0)
    #: Atributo condicional para expresar el total de los impuestos trasladados que se desprenden de los conceptos
    #: expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando
    #: en los conceptos se registren impuestos trasladados.
    total_impuestos_trasladados: NonNegativeSixDecimals = Decimal(0)

    _to_array = reusable_validator("traslados", "retenciones", pre=True)(dict2list_flatten)


class CfdiRelacionado(BaseModel):
    """
    Schema of a "Cfdi Relacionado" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para registrar el folio fiscal (UUID) de un CFDI relacionado con el presente comprobante,
    #: por ejemplo: Si el CFDI relacionado es un comprobante de traslado que sirve para registrar el movimiento de la
    #: mercancía. Si este comprobante se usa como nota de crédito o nota de débito del comprobante relacionado.
    #: Si este comprobante es una devolución sobre el comprobante relacionado. Si éste sustituye a una factura
    #: cancelada.
    uuid: UUID


class CfdiRelacionados(BaseModel):
    """
    Schema of a "Cfdi Relacionados" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    #: Atributo requerido para indicar la clave de la relación que existe entre éste que se esta generando y el o
    #: los CFDI previos.
    tipo_relacion: TipoRelacion
    #: Cfdi Relacionado
    cfdi_relacionado: List[CfdiRelacionado]

    _to_array = reusable_validator("cfdi_relacionado", pre=True)(dict2list)


class CFDI33(BaseModel, CFDIMixin):
    """
    Schema of a CFDI version 3.3.

    Based on:

    * https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    * https://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd
    * https://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    #: Atributo requerido con valor prefijado a 3.3 que indica la versión del estándar bajo el que se encuentra
    #: expresado el comprobante.
    version: Literal["3.3"]
    #: Atributo opcional para precisar la serie para control interno del contribuyente. Este atributo acepta
    #: una cadena de caracteres
    serie: Optional[Annotated[str, Field(min_length=1, max_length=25, regex=r"[^|]{1,25}")]]
    #: Atributo opcional para control interno del contribuyente que expresa el folio del comprobante, acepta una
    #: cadena de caracteres.
    folio: Optional[Annotated[str, Field(min_length=1, max_length=40, regex=r"[^|]{1,40}")]]
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
    no_certificado: Annotated[str, Field(min_length=1, max_length=20, regex=r"[0-9]{20}")]
    #: Atributo requerido que sirve para incorporar el certificado de sello digital que ampara al comprobante, como
    #: texto en formato base 64.
    certificado: str
    #: Atributo condicional para expresar las condiciones comerciales aplicables para el pago del comprobante fiscal
    #: digital por Internet. Este atributo puede ser condicionado mediante atributos o complementos.
    condiciones_de_pago: Optional[Annotated[str, Field(min_length=1, max_length=1000, regex=r"[^|]{1,1000}")]]
    #: Atributo requerido para representar la suma de los importes de los conceptos antes de descuentos e impuesto.
    #: No se permiten valores negativos.
    sub_total: NonNegativeSixDecimals
    #: Atributo condicional para representar el importe total de los descuentos aplicables antes de impuestos. No se
    #: permiten valores negativos. Se debe registrar cuando existan conceptos con descuento.
    descuento: NonNegativeSixDecimals = Decimal(0)
    #: Atributo requerido para identificar la clave de la moneda utilizada para expresar los montos, cuando se usa
    #: moneda nacional se registra MXN. Conforme con la especificación ISO 4217.
    moneda: Moneda
    #: Atributo condicional para representar el tipo de cambio conforme con la moneda usada. Es requerido cuando la
    #: clave de moneda es distinta de MXN y de XXX. El valor debe reflejar el número de pesos mexicanos que equivalen
    #: a una unidad de la divisa señalada en el atributo moneda. Si el valor está fuera del porcentaje aplicable a la
    #: moneda tomado del catálogo c_Moneda, el emisor debe obtener del PAC que vaya a timbrar el CFDI, de manera no
    #: automática, una clave de confirmación para ratificar que el valor es correcto e integrar dicha clave en el
    #: atributo Confirmacion.
    tipo_cambio: Optional[PositiveSixDecimals]
    #: Atributo requerido para representar la suma del subtotal, menos los descuentos aplicables, más las contribuciones
    #: recibidas (impuestos trasladados - federales o locales, derechos, productos, aprovechamientos, aportaciones de
    #: seguridad social, contribuciones de mejoras) menos los impuestos retenidos. Si el valor es superior al límite que
    #: establezca el SAT en la Resolución Miscelánea Fiscal vigente, el emisor debe obtener del PAC que vaya a timbrar
    #: el CFDI, de manera no automática, una clave de confirmación para ratificar que el valor es correcto e integrar
    #: dicha clave en el atributo Confirmacion. No se permiten valores negativos.
    total: NonNegativeSixDecimals
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
    confirmacion: Optional[Annotated[str, Field(min_length=5, max_length=5, regex=r"[0-9a-zA-Z]{5}")]]
    #: Nodo opcional para precisar la información de los comprobantes relacionados.
    cfdi_relacionados: Optional[CfdiRelacionados]
    #: Nodo requerido para expresar la información del contribuyente emisor del comprobante.
    emisor: Emisor
    #: Nodo requerido para precisar la información del contribuyente receptor del comprobante
    receptor: Receptor
    #: Nodo requerido para listar los conceptos cubiertos por el comprobante.
    conceptos: List[Concepto]
    #: Nodo condicional para expresar el resumen de los impuestos aplicables.
    impuestos: Optional[ImpuestosCFDI]
    #: Nodo opcional donde se incluye el complemento Timbre Fiscal Digital de manera obligatoria y los nodos
    #: complementarios determinados por el SAT, de acuerdo con las disposiciones particulares para un sector o
    #: actividad específica.
    complemento: List[ComplementoType] = []
    #: Nodo opcional para recibir las extensiones al presente formato que sean de utilidad al contribuyente.
    #: Para las reglas de uso del mismo, referirse al formato origen.
    addenda: Optional[Dict]

    _to_array = reusable_validator("complemento", "conceptos", pre=True)(dict2list_flatten)
