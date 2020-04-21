from math import comb

import pytest

from .algorithm import (
    create_all_combinations,
    create_combinations_with_itertools,
)
from .basket import Item


@pytest.fixture
def items():
    return [
        Item(1),
        Item(2),
        Item(3),
        Item(4),
        Item(5),
    ]


def test_generate_all_combinations_returns_proper_amount(items):
    items_len = len(items)
    combinations = create_all_combinations(items)
    expected_output = sum([comb(items_len, i) for i in range(1, items_len + 1)])
    assert len(combinations) == expected_output


def test_generate_all_combinations_with_itertools(items):
    items_len = len(items)
    combinations = create_combinations_with_itertools(items)
    expected_output = sum([comb(items_len, i) for i in range(1, items_len + 1)])
    assert len(combinations) == expected_output
