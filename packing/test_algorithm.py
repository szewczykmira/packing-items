from math import comb

from .algorithm import create_all_combinations
from .basket import Item


def test_generate_all_combinations_returns_proper_amount():
    items = [
        Item(1),
        Item(2),
        Item(3),
        Item(4),
        Item(5),
    ]
    items_len = len(items)
    combinations = create_all_combinations(items)
    expected_output = sum([comb(items_len, i) for i in range(1, items_len + 1)])
    assert len(combinations) == expected_output
