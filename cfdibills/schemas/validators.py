"""
Validators used to parse CFDIs.
"""

from typing import Union

from pydantic import validator


def dict2list(original: Union[dict, list]) -> list:
    assert isinstance(original, (dict, list)), "Unsupported type. Must be 'list' or 'dict'"
    return [original] if isinstance(original, dict) else original


def dict2list_flatten(original: Union[dict, list]) -> list:
    if isinstance(original, dict):
        result = []
        for key, value in original.items():
            if isinstance(value, dict):
                result += [value]
            elif isinstance(value, list):
                result += [t for t in value]
            else:
                raise ValueError(f"Unsupported type in {key}. Must be 'list' or 'dict'")
    elif isinstance(original, list):
        result = original
    elif original is None:
        result = []
    else:
        raise ValueError("Unsupported type. Must be 'list' or 'dict'")
    return result


def reusable_validator(*args, **kwargs):
    return validator(*args, **kwargs, allow_reuse=True)
