import xmltodict
from .utils.parsing import normalize_dict_keys

def read_xml(path: str) -> dict:
    """
    Reads a CFDI in a .xml and maps it to a python object

    Args
        path: path to the xml to read
        validate: if the xml should be tested to be a valid CFDI or not
    """
    # Try for the possible cfdi versions
    with open(path, 'rb') as f:
        try:
            raw_xml = xmltodict.parse(f, dict_constructor=dict)
            return normalize_dict_keys(raw_xml)["comprobante"]
        except:
            raise ValueError(f"Could not read '{path}'. Make sure it is a valid CFDI.")