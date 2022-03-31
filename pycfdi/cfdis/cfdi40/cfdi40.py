from .. import base_cfdi
import xmlschema
from pathlib import Path

class CFDI40(base_cfdi.CFDI):

    def build_schema(self):
        this_path = Path(__file__).parent
        namespaces = ["schema/TimbreFiscalDigitalv11.xsd", "schema/cfdv40.xsd"]
        return xmlschema.XMLSchema([this_path / name for name in namespaces])

    def get_version(self):
        return "4.0"