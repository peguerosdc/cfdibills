from abc import ABC, abstractmethod
import re

_name_pattern = re.compile(r'(.)([A-Z][a-z]+)')
_snake_pattern = re.compile(r'([a-z0-9])([A-Z])')

def _camel_to_snake(camelcase: str) -> str:
    """
    Converts a camelCase string to a snake_case string
    Source: https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case

    Args:
        camelcase: string to convert
    
    Returns: snake_cased string
    """
    camelcase = _name_pattern.sub(r'\1_\2', camelcase)
    return _snake_pattern.sub(r'\1_\2', camelcase).lower()

def _normalize_dict_keys(ugly_dict: dict) -> dict:
    """
    Maps the raw keys of a xmlschema to human readable keys

    xmlschema returns a dict with keys that:
    
    * begin with "@" when they are leaf nodes
    * begin with "cfdi:", "tfd:" or similar when they are nodes
    * contain "xmlns" and "xsi" when are namespace definition
    * are written in camelCase as defined by SAT's xsd

    So all of these are normalized to plain snake_case strings
    """
    result = dict()
    # normalization techniques of items where:
    # * if the item is a dictionary, normalize its children
    # * if it is an array, normalize every item in it
    normalization = dict()
    normalization[list] = lambda x: [_normalize_dict_keys(y) for y in x]
    normalization[dict] = lambda x: _normalize_dict_keys(x)
    # normalize key by key in a DFS way
    for key, value in ugly_dict.items():
        # namespaces are not part of cfdi's, so they are omitted
        if "xmlns" not in key and "xsi" not in key:
            # get the normalized version of this key removing unwanted chars
            new_key = _camel_to_snake(key[1:] if "@" in key else key.split(":")[-1])
            # normalize the item
            result[new_key] = normalization[type(value)](value) if type(value) in normalization else value
    return result

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
        cfdi = _normalize_dict_keys(raw_dict)
        return cfdi