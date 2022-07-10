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
    if isinstance(original, dict):
        result = []
        for key, value in original.items():
            if isinstance(value, dict):
                result += [{**value, "tipo": key}]
            elif isinstance(value, list):
                result += [{**t, "tipo": key} for t in value]
    else:
        result = original
    return result


def parse_fecha(fecha: str) -> datetime:
    return datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")


def is_positive(value):
    if value < 0:
        raise ValueError(f"Must be a positive number")
    return value


def reusable_validator(*args, **kwargs):
    return validator(*args, **kwargs, allow_reuse=True)
