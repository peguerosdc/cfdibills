from datetime import datetime

import pytest
from pytest import mark

from cfdibills.cfdis.validators import (
    dict2list_flatten,
    is_positive,
    parse_fecha,
    validate_length,
)
from tests.utils import does_not_raise


@mark.parametrize(
    "value, min_length, max_length, raises, expected",
    [
        ("abc", 1, 5, does_not_raise(), "abc"),
        (
            "abc",
            1,
            2,
            pytest.raises(ValueError, match=r".*(min_length=\d and max_length=\d).*"),
            None,
        ),
        (
            "abc",
            2,
            2,
            pytest.raises(ValueError, match=r".*(Must be of length=\d).*"),
            None,
        ),
    ],
)
def test_validate_length(value, min_length, max_length, raises, expected):
    with raises:
        result = validate_length(min_length, max_length)(value)
        assert result == expected


def test_parse_fecha():
    assert parse_fecha("2022-07-10T01:15:35") == datetime(2022, 7, 10, 1, 15, 35)


@mark.parametrize(
    "value, raises",
    [
        (5, does_not_raise()),
        (-1, pytest.raises(ValueError)),
    ],
)
def test_validate_is_positive(value, raises):
    with raises:
        assert value == is_positive(value)


@mark.parametrize(
    "original, expected",
    [
        ([{"impuesto": "traslado1"}], [{"impuesto": "traslado1"}]),
        (
            {"traslado": {"a": {"aa": 1}, "b": {"bb": 1}}},
            [
                {
                    "a": {"aa": 1},
                    "b": {"bb": 1},
                },
            ],
        ),
        ({"traslado": [{"a": 3, "b": 4}]}, [{"a": 3, "b": 4}]),
    ],
)
def test_dict2list(original, expected):
    assert dict2list_flatten(original) == expected
