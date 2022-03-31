from abc import ABC, abstractmethod
from ..utils import normalize_dict_keys

class CFDI(ABC):

    def __init__(self):
        self.xmlschema = self.build_schema()
        self.version = self.get_version()
    
    @abstractmethod
    def build_schema(self):
        pass
    
    @abstractmethod
    def get_version(self):
        pass

    def validate(self, xml_path: str) -> bool:
        return self.xmlschema.is_valid(xml_path)

    def read(self, xml_path: str) -> dict:
        raw_dict = self.xmlschema.to_dict(xml_path)
        cfdi = normalize_dict_keys(raw_dict)
        return cfdi