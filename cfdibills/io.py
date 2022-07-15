"""
Module to read CFDIs.
"""

from __future__ import annotations

import re
from decimal import Decimal
from typing import Callable, Type, Union

import pydantic
import xmltodict

from cfdibills.errors import InvalidCFDIError, UnsupportedCFDIError
from cfdibills.schemas.cfdi33 import CFDI33
from cfdibills.schemas.cfdi40 import CFDI40

_name_pattern = re.compile(r"(.)([A-Z][a-z]+)")
_snake_pattern = re.compile(r"([a-z0-9])([A-Z])")


def _get_cfdi_with_version(candidate: dict) -> tuple[dict, str]:
    try:
        cfdi = candidate["comprobante"]
        version = cfdi["version"]
    except KeyError as e:
        raise InvalidCFDIError(f"The XML given does not contain a '{e.args[0]}'.")
    return cfdi, version


def _xml_to_json(path: str, normalize: bool = True) -> dict:
    with open(path, "rb") as f:
        raw_xml = xmltodict.parse(f, dict_constructor=dict)
    return normalize_dict_keys(raw_xml) if normalize else raw_xml


def _parse_cfdi(cfdi: dict, version: str) -> Union[CFDI33, CFDI40]:
    mapper = {"3.3": CFDI33, "4.0": CFDI40}
    if (parser := mapper.get(version, None)) is None:
        raise UnsupportedCFDIError(f"Version '{version}' is not supported. It must be one of {mapper.keys()}.")
    try:
        # Mypy doesn't know that the parser is also of type BaseModel, so we have to tell it to ignore this line
        parsed = parser.parse_obj(cfdi)  # type: ignore
    except pydantic.ValidationError as e:
        raise InvalidCFDIError(str(e)) from None
    return parsed


def _camel_to_snake(camelcase: str) -> str:
    """
    Converts a camelCase string to a snake_case string
    Source: https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case

    Parameters
    ----------
    camelcase: str
        string to convert

    Returns
    -------
    str
        snake_cased string
    """
    camelcase = _name_pattern.sub(r"\1_\2", camelcase)
    return _snake_pattern.sub(r"\1_\2", camelcase).lower()


def normalize_dict_keys(ugly_dict: dict) -> dict:
    """
    Maps the raw keys of a xmlschema to human-readable keys.

    xmlschema returns a dict with keys that:

    * begin with "@" when they are leaf nodes
    * begin with "cfdi:", "tfd:" or similar when they are nodes
    * contain "xmlns" and "xsi" when are namespace definition
    * are written in camelCase as defined by SAT's xsd

    So all of these are normalized to plain snake_case strings

    Some special cases:

    * if the item is a Decimal, map it to a float python number
    * if the item is a dictionary, normalize its children
    * if it is an array, normalize every item in it

    Parameters
    ----------
    ugly_dict: dict
        Dictionary as output from xmltodict

    Returns
    -------
    dict
        Dictionary with keys in camel_case format
    """
    result = dict()
    normalization: dict[Type[Union[list, dict, Decimal]], Callable] = {
        list: lambda x: [normalize_dict_keys(y) for y in x],
        dict: lambda x: normalize_dict_keys(x),
        Decimal: lambda x: float(x),
    }
    # normalize key by key in a DFS way
    for key, value in ugly_dict.items():
        # namespaces are not part of cfdi's, so they are omitted
        if "xmlns" not in key and "xsi" not in key:
            # get the normalized version of this key removing unwanted chars
            new_key = _camel_to_snake(key[1:] if "@" in key else key.split(":")[-1])
            # normalize the item
            result[new_key] = normalization[type(value)](value) if type(value) in normalization else value
    return result


def read_xml(path: str) -> Union[CFDI33, CFDI40]:
    """
    Reads a CFDI in a .xml and maps it to a pydantic object.

    Parameters
    ----------
    path: path to the xml file to read

    Returns
    -------
    Union[CFDI33, CFDI40]
        Pydantic object of the CFDI

    Raises
    ------
    InvalidCFDIError
        If the xml is not in a valid format
    UnsupportedCFDIError
        If the CFDI version of the XML is not supported
    """
    normalized_xml = _xml_to_json(path)
    cfdi, version = _get_cfdi_with_version(normalized_xml)
    return _parse_cfdi(cfdi, version)
