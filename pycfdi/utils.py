from .cfdis import *
from typing import Union

def is_cfdi(path: str) -> Union[str, bool]:
    """
    Validates if the given xml is a valid CFDI or not

    Args:
        path: path to the xml to validate
    """
    # Try for the possible cfdi versions
    versions = [cfdi33]
    for cfdi_version in versions:
        if cfdi_version.validate(path):
            return cfdi_version.version
    return False