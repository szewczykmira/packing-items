from math import comb  # type: ignore

from .. import naive, with_itertools


def test_generate_all_combinations_returns_proper_amount(items):
    items_len = len(items)
    combinations = naive.create_all(items)
    expected_output = sum([comb(items_len, i) for i in range(1, items_len + 1)])
    assert len(combinations) == expected_output


def test_generate_all_combinations_with_itertools(items):
    items_len = len(items)
    combinations = with_itertools.create_all(items)
    expected_output = sum([comb(items_len, i) for i in range(1, items_len + 1)])
    assert len(combinations) == expected_output
