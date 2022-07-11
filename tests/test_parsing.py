from devtools import debug
from pytest import mark

from cfdibills import read_xml
from cfdibills.cfdis.complementos import (
    Aerolineas,
    CertificadoDeDestruccion,
    ComercioExterior,
)
from tests.utils import does_not_raise


@mark.parametrize(
    "path, complement_type",
    [
        ("tests/samples/aerolineas.xml", Aerolineas),
        ("tests/samples/certificado_de_destruccion.xml", CertificadoDeDestruccion),
        ("tests/samples/comercio_exterior.xml", ComercioExterior),
    ],
)
def test_aerolineas(path, complement_type):
    with does_not_raise():
        cfdi = read_xml(path)
        debug(cfdi)
        cfdi.get_complemento(complement_type)
