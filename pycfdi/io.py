from typing import Union
from .cfdis import cfdi_schemas

def read_xml(path: str) -> dict:
    """
    Reads a CFDI in a .xml and maps it to a python object

    Args
        path: path to the xml to read
        validate: if the xml should be tested to be a valid CFDI or not
    """
    # Try for the possible cfdi versions
    for cfdi_version in cfdi_schemas:
        if cfdi_version.validate(path):
            return cfdi_version.read(path)
    raise ValueError(f"File '{path}' is not a valid cfid")

def is_cfdi(path: str) -> Union[str, bool]:
    """
    Validates if the given xml is a valid CFDI or not

    Args:
        path: path to the xml to validate
    """
    # Try for the possible cfdi versions
    for cfdi_version in cfdi_schemas:
        if cfdi_version.validate(path):
            return cfdi_version.version
    return False