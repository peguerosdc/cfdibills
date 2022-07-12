"""
Validators used to parse CFDIs.
"""

from datetime import datetime
from typing import Union

from pydantic import validator


def validate_length(min_length: int, max_length: int):
    def fn(value: str):
        length = len(value)
        if not (min_length <= length <= max_length):
            if min_length == max_length:
                raise ValueError(f"Must be of length={min_length}")
            else:
                raise ValueError(f"{length=} but {min_length=} and {max_length=}")
        return value

    return fn


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
    else:
        raise ValueError("Unsupported type. Must be 'list' or 'dict'")
    return result


def parse_fecha(fecha: str) -> datetime:
    return datetime.strptime(str(fecha), "%Y-%m-%dT%H:%M:%S")


def is_positive(value):
    if value < 0:
        raise ValueError("Must be a positive number")
    return value


def reusable_validator(*args, **kwargs):
    return validator(*args, **kwargs, allow_reuse=True)
