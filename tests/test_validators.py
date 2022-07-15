from datetime import datetime

import pytest
from pytest import mark

from cfdibills.schemas.validators import dict2list_flatten


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
