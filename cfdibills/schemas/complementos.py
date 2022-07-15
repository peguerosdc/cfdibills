"""
Complementos available to appear in a CFDI.
"""

from datetime import datetime
from typing import Dict, List, Optional, TypeVar, Union
from uuid import UUID

from pydantic import BaseModel

from cfdibills.schemas.validators import (
    dict2list,
    dict2list_flatten,
    reusable_validator,
)


class TimbreFiscalDigital(BaseModel):
    """
    Complemento requerido para el Timbrado Fiscal Digital que da validez al Comprobante fiscal digital por Internet.

    https://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd
    """

    #: Atributo requerido para la expresión de la versión del estándar del Timbre Fiscal Digital
    version: str
    #: Atributo requerido para expresar los 36 caracteres del folio fiscal (UUID) de la transacción de timbrado
    #: conforme al estándar RFC 4122
    uuid: UUID
    #: Atributo requerido para expresar la fecha y hora, de la generación del timbre por la certificación digital del
    #: SAT. Se expresa en la forma AAAA-MM-DDThh:mm:ss y debe corresponder con la hora de la Zona Centro del
    #: Sistema de Horario en México.
    fecha_timbrado: datetime
    #: Atributo requerido para expresar el RFC del proveedor de certificación de comprobantes fiscales digitales que
    #: genera el timbre fiscal digital.
    rfc_prov_certif: str
    #: Atributo opcional para registrar información que el SAT comunique a los usuarios del CFDI.
    leyenda: Optional[str]
    #: Atributo requerido para contener el sello digital del comprobante fiscal o del comprobante de retenciones,
    #: que se ha timbrado. El sello debe ser expresado como una cadena de texto en formato Base 64.
    sello_cfd: str
    #: Atributo requerido para expresar el número de serie del certificado del SAT usado para generar el sello digital
    #: del Timbre Fiscal Digital.
    no_certificado_sat: str
    #: Atributo requerido para contener el sello digital del Timbre Fiscal Digital, al que hacen referencia las reglas
    #: de la Resolución Miscelánea vigente. El sello debe ser expresado como una cadena de texto en formato Base 64.
    sello_sat: str


class Aerolineas(BaseModel):
    """
    Complemento al Comprobante Fiscal Digital a través de Internet (CFDI) para el manejo de datos de Aerolíneas para
    pasajeros.

    https://www.sat.gob.mx/sitio_internet/cfd/aerolineas/aerolineas.xsd
    """

    class OtrosCargos(BaseModel):
        """
        Seccion OtrosCargos dentro del complemento Aerolineas
        """

        class Cargo(BaseModel):
            """
            Seccion Cargo dentro del complemento OtrosCargos
            """

            #: Atributo requerido para indicar el código del cargo según el catálogo de la IATA.
            codigo_cargo: str
            #: Atributo requerido para representar el importe del cargo.
            importe: float

        #: Atributo requerido para expresar el total de los cargos adicionales que se están aplicando.
        total_cargos: float
        cargo: List[Cargo]

        _to_array = reusable_validator("cargo", pre=True)(dict2list)

    #: Atributo requerido para la expresión de la versión del complemento
    version: str
    #: Atributo requerido para indicar el importe del TUA aplicable al boleto.
    tua: float
    #: Tipo definido para expresar importes numéricos con fracción hasta seis decimales
    importe: float
    #: Nodo opcional para expresar otros cargos aplicables
    otros_cargos: Optional[OtrosCargos]


class CertificadoDeDestruccion(BaseModel):
    """
    Complemento para incorporar la información que integra el certificado de destrucción de vehículos destruidos por
    los centros de destrucción autorizados por el SAT.

    http://www.sat.gob.mx/sitio_internet/cfd/certificadodestruccion/certificadodedestruccion.xsd
    """

    class VehiculoDestruido(BaseModel):
        #: Atributo requerido para expresar la marca del vehículo que se destruyó.
        marca: str
        #: Atributo requerido para expresar el tipo o clase del vehículo que se destruyó.
        tipoo_clase: str
        #: Atributo requerido para la expresión del año del vehículo.
        año: int
        #: Atributo opcional para expresar el modelo del vehículo que se destruyó.
        modelo: Optional[str]
        #: Atributo opcional para expresar el número de identificación vehicular del vehículo (Cuando exista el NIV
        #: deberá incluirse este invariablemente).
        niv: Optional[str]
        #: Atributo opcional para expresar el número de serie de la carrocería del vehículo (en caso de contar con
        #: dicho número se deberá ingresar)
        num_serie: Optional[str]
        #: Atributo requerido para expresar el número de placas metálicas de identificación del servicio público
        #: federal o, en su caso, del servicio público de autotransporte de pasajero urbano o suburbano.
        num_placas: str
        #: Atributo opcional para expresar el número de motor del vehículo (en caso de contar con dicho número se
        #: deberá ingresar).
        num_motor: Optional[str]
        #: Atributo requerido para expresar el número de folio de la tarjeta de circulación.
        num_fol_tarj_cir: str

    class InformacionAduanera(BaseModel):
        #: Atributo requerido para expresar el número de documento aduanero que ampara la importación del vehículo
        #: a destruir.
        num_ped_imp: str
        #: Atributo requerido para expresar la fecha de expedición del documento aduanero que ampara la importación
        #: del vehículo a destruir.
        fecha: datetime
        #: Atributo requerido para precisar la aduana a través de la cual se regularizó la legal estancia en el país
        #: del vehículo destruido.
        aduana: str

    #: Atributo requerido para la expresión de la versión del complemento
    version: str
    #: Atributo requerido para expresar la serie de acuerdo al catálogo.
    serie: str
    #: Atributo requerido que expresa el número de folio para la destrucción del vehículo emitido por el Servicio de
    #: Administración Tributaria.
    num_fol_des_veh: str
    #: Nodo requerido para expresar la información del vehículo que se destruyó.
    vehiculo_destruido: VehiculoDestruido
    #: Nodo opcional para expresar la información aduanera aplicable cuando se trate de un vehículo importado que
    #: se destruyó.
    informacion_aduanera: Optional[InformacionAduanera]


class ComercioExteriorDomicilio(BaseModel):
    calle: str
    numero_exterior: Optional[str]
    numerio_interior: Optional[str]
    colonia: Optional[str]
    localidad: Optional[str]
    referencia: Optional[str]
    municipio: Optional[str]
    estado: str
    pais: str
    codigo_postal: str


class ComercioExterior(BaseModel):
    """
    Complemento para incorporar la información en el caso de Exportación de Mercancías en definitiva.

    http://www.sat.gob.mx/sitio_internet/cfd/ComercioExterior11/ComercioExterior11.xsd
    """

    class Emisor(BaseModel):

        domicilio: Optional[ComercioExteriorDomicilio]
        #: Atributo condicional para expresar la CURP del emisor del CFDI cuando es una persona física.
        curp: Optional[str]

    class Receptor(BaseModel):
        domicilio: Optional[ComercioExteriorDomicilio]
        num_reg_id_trib: Optional[str]

    class Propietario(BaseModel):
        #: Atributo requerido para incorporar el número de identificación o registro fiscal del país de residencia para
        #: efectos fiscales del propietario de la mercancía trasladada.
        num_reg_id_trib: str
        #: Atributo requerido para registrar la clave del país de residencia para efectos fiscales del propietario de
        #: la mercancía, conforme con el catálogo c_Pais publicado en el portal del SAT en internet que está basado en
        #: la especificación ISO 3166-1.
        residencia_fiscal: str

    class Destinatario(BaseModel):
        #: Nodo requerido para expresar el domicilio del destinatario de la mercancía.
        domicilio: List[ComercioExteriorDomicilio]
        #: Atributo opcional para incorporar el número de identificación o registro fiscal del país de residencia para
        #: efectos fiscales del destinatario de la mercancía exportada.
        num_reg_id_trib: Optional[str]
        #: Atributo opcional para expresar el nombre completo, denominación o razón social del destinatario de la
        #: mercancía exportada.
        nombre: Optional[str]

    class Mercancia(BaseModel):
        class DescripcionEspecifica(BaseModel):
            #: Atributo requerido que indica la marca de la mercancía.
            marca: str
            #: Atributo opcional que indica el modelo de la mercancía.
            modelo: Optional[str]
            #: Atributo opcional que indica el submodelo de la mercancía.
            sub_modelo: Optional[str]
            #: Atributo opcional que indica el número de serie de la mercancía.
            numero_serie: Optional[str]

        #: Atributo requerido que sirve para expresar el número de parte, la clave de identificación que asigna la
        #: empresa o el número de serie de la mercancía exportada.
        no_identificacion: str
        #: Atributo condicional que sirve para expresar la clave de la fracción arancelaria correspondiente a la
        #: descripción de la mercancía exportada, este dato se vuelve requerido cuando se cuente con él o se esté
        #: obligado legalmente a contar con él.Debe ser conforme con el catálogo c_FraccionArancelaria publicado en el
        #: portal del SAT en internet.
        fraccion_arancelaria: Optional[str]
        #: Atributo opcional para precisar la cantidad de bienes en la aduana conforme a la UnidadAduana cuando en el
        #: nodo Comprobante:Conceptos:Concepto se hubiera registrado información comercial.
        cantidad_aduana: Optional[float]
        #: Atributo condicional para precisar la clave de la unidad de medida aplicable para la cantidad expresada en
        #: la mercancía en la aduana, conforme con el catálogo c_UnidadAduana publicado en el portal del SAT en
        #: internet.
        unidad_aduana: Optional[str]
        #: Atributo condicional para precisar el valor o precio unitario del bien en la aduana. Se expresa en dólares
        #: de Estados Unidos (USD), el cual puede estar registrado hasta centésimas.
        valor_unitario_aduana: Optional[float]
        #: Atributo requerido que indica el valor total en dólares de Estados Unidos (USD).
        valor_dolares: float
        #: Nodo opcional que indica la lista de descripciones específicas de la mercancía.
        #: Una mercancía puede tener más de una descripción específica.
        descripciones_especificas: List[DescripcionEspecifica] = []

        _to_array = reusable_validator("descripciones_especificas", pre=True)(dict2list)

    emisor: Optional[Emisor]
    #: Nodo condicional para capturar los datos del o los propietarios de la mercancía que se traslada y ésta no sea
    #: objeto de enajenación o siéndolo sea a título gratuito, cuando el emisor del CFDI es un tercero.
    propietario: List[Propietario] = []
    #: Nodo condicional para capturar los datos complementarios del receptor del CFDI.
    receptor: Optional[Receptor]
    #: Nodo opcional para capturar los datos del destinatario de la mercancía cuando éste sea distinto del receptor
    #: del CFDI.
    destinatario: Optional[Destinatario]
    #: Nodo condicional para capturar la información de la declaración de las mercancías exportadas.
    mercancias: List[Mercancia] = []
    #: Atributo requerido que indica la versión del complemento.
    version: str
    #: Atributo condicional que indica la clave del motivo por el cual en la exportación definitiva de mercancías con
    #: clave de pedimento A1, éstas no son objeto de enajenación o siéndolo sean a título gratuito, desde el domicilio
    #: del emisor hacia el domicilio del receptor o del destinatario. La clave del motivo es conforme con el catálogo
    #: c_MotivoTraslado publicado en el portal del SAT en internet.
    motivo_traslado: Optional[str]
    #: Atributo requerido que indica la clave del tipo de operación de Comercio Exterior que se realiza, conforme con
    #: el catálogo c_TipoOperacion publicado en el portal del SAT en internet.
    tipo_operacion: str
    #: Atributo condicional que indica la clave de pedimento que se haya declarado conforme con el catálogo c
    #: ClavePedimento publicado en el portal del SAT en internet.
    clave_de_pedimento: Optional[str]
    #: Atributo condicional derivado de la excepción de certificados de Origen de los Tratados de Libre Comercio que ha
    #: celebrado México con diversos países. 0 = No Funge como certificado de origen 1 = Funge como certificado de
    #: origen.
    certificado_origen: Optional[int]
    #: Atributo condicional para expresar el folio del certificado de origen o el folio fiscal del CFDI con el que se
    #: pagó la expedición del certificado de origen.
    num_certificado_origen: Optional[str]
    #: Atributo condicional que indica el número de exportador confiable, conforme al artículo 22 del Anexo 1 del
    #: Tratado de Libre Comercio con la Asociación Europea y a la Decisión de la Comunidad Europea.
    num_exportador_confiable: Optional[str]
    #: Atributo condicional que indica la clave del INCOTERM aplicable a la factura, conforme con el catálogo
    #: c_INCOTERM publicado en el portal del SAT en internet.
    incoterm: Optional[str]
    #: Atributo condicional que indica si la factura tiene o no subdivisión. Valores posibles: 0 - no tiene
    #: subdivisión,1 - si tiene subdivisión.
    subdivision: Optional[int]
    #: Atributo opcional en caso de ingresar alguna información adicional, como alguna leyenda que debe incluir en
    #: el CFDI.
    observaciones: Optional[str]
    #: Atributo condicional que indica el número de pesos mexicanos que equivalen a un dólar de Estados Unidos, de
    #: acuerdo al artículo 20 del Código Fiscal de la Federación.
    tipo_cambio_usd: Optional[str]
    #: Atributo condicional que indica el importe total del comprobante en dólares de Estados Unidos.
    total_usd: Optional[float]

    _to_array = reusable_validator("mercancias", pre=True)(dict2list_flatten)


ComplementoType = Union[TimbreFiscalDigital, Aerolineas, CertificadoDeDestruccion, ComercioExterior, Dict]
AnyComplementoType = TypeVar("AnyComplementoType", bound=ComplementoType)
