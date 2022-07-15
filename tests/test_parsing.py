from devtools import debug
from pytest import mark

from cfdibills import read_xml
from cfdibills.schemas.cfdi33 import CFDI33
from cfdibills.schemas.cfdi40 import CFDI40
from cfdibills.schemas.complementos import (
    Aerolineas,
    CertificadoDeDestruccion,
    ComercioExterior,
)
from tests.utils import does_not_raise


@mark.parametrize(
    "path, cfdi_type",
    [
        ("tests/samples/cfdv40-min.xml", CFDI40),
        ("tests/samples/cfdv40-ejemplo.xml", CFDI40),
        ("tests/samples/cfdv40-ejemplo-signed-tfd.xml", CFDI40),
        ("tests/samples/cfdv33-base.xml", CFDI33),
        ("tests/samples/cfdv33-min.xml", CFDI33),
        ("tests/samples/cfdv33-signed-tfd.xml", CFDI33),
    ],
)
def test_cfdis(path, cfdi_type):
    with does_not_raise():
        cfdi = debug(read_xml(path))
        assert isinstance(cfdi, cfdi_type)


@mark.parametrize(
    "path, complement_type",
    [
        ("tests/samples/aerolineas.xml", Aerolineas),
        ("tests/samples/certificado_de_destruccion.xml", CertificadoDeDestruccion),
        ("tests/samples/comercio_exterior.xml", ComercioExterior),
    ],
)
def test_complementos(path, complement_type):
    with does_not_raise():
        cfdi = debug(read_xml(path))
        cfdi.get_complemento(complement_type)
