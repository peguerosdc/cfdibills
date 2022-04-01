from .. import base_cfdi
import xmlschema
from pathlib import Path

class CFDI33(base_cfdi.CFDI):

    def build_schema(self):
        this_path = Path(__file__).parent
        namespaces = ["schema/TimbreFiscalDigitalv11.xsd", "schema/cfdv33.xsd"]
        return xmlschema.XMLSchema([this_path / name for name in namespaces])

    def get_version(self):
        return "3.3"