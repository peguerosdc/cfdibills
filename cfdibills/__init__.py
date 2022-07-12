"""
cfdibills main package
"""
from .io import read_xml
from .verifiers import verify


def _get_version() -> str:
    """
    Get package version.

    Returns
    -------
    version : str
    """
    from os.path import dirname, join

    with open(join(dirname(__file__), "VERSION")) as f:
        return f.read().strip()


__version__ = _get_version()
