from __future__ import annotations

import xmltodict

from cfdis.cfdi33 import CFDI33
from utils import normalize_dict_keys


def _get_cfdi_with_version(candidate: dict) -> tuple[dict, str]:
    try:
        cfdi = candidate["comprobante"]
        version = cfdi["version"]
    except KeyError as e:
        raise ValueError(f"The XML given does not contain a {e.args[0]}")
    return cfdi, version


def _parse_cfdi(cfdi: dict, version: str) -> CFDI33:
    mapper = {"3.3": CFDI33}
    if (parser := mapper.get(version, None)) is None:
        raise ValueError(
            f"Version {version} is not supported. It must be one of {mapper.keys()}."
        )
    return parser.parse_obj(cfdi)


def read_xml(path: str) -> CFDI33:
    """
    Reads a CFDI in a .xml and maps it to a python object.

    Parameters
    ----------
    path: path to the xml file to read

    Returns
    -------
    CFDI33
    """
    with open(path, "rb") as f:
        raw_xml = xmltodict.parse(f, dict_constructor=dict)
    normalized_xml = normalize_dict_keys(raw_xml)
    cfdi, version = _get_cfdi_with_version(normalized_xml)
    return _parse_cfdi(cfdi, version)
