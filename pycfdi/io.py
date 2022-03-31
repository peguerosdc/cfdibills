from .cfdis import *

def read_xml(path: str) -> dict:
    """
    Reads a CFDI in a .xml and maps it to a python object

    Args
        path: path to the xml to read
        validate: if the xml should be tested to be a valid CFDI or not
    """
    # Try for the possible cfdi versions
    versions = [cfdi33]
    for cfdi_version in versions:
        if cfdi_version.validate(path):
            return cfdi_version.read(path)
    raise ValueError(f"File '{path}' is not a valid cfid")
