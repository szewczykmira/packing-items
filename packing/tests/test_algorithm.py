import pytest

from ..algorithm_v3 import get_affordable_baskets as get_affordable_baskets_v3
from ..algorithm_v12 import get_affordable_baskets
from ..combinations_v2 import create_all


@pytest.fixture
def baskets_combinations(items):
    return create_all(items)


def test_affordable_baskets_only_equal(baskets_combinations):
    result = list(get_affordable_baskets(10, baskets_combinations))
    assert len(result) == 3
    assert all(basket.cost == 10 for basket in result)


def test_affordable_baskets_lt(baskets_combinations):
    result = list(get_affordable_baskets(10, baskets_combinations, lte=True))
    assert all(basket.cost <= 10 for basket in result)


def test_affordable_baskets_v3_only_equal(items):
    result = get_affordable_baskets_v3(10, items)
    assert len(result) == 3
    assert all(basket.cost == 10 for basket in result)


def test_affordable_baskets_v3_lt(items):
    result = get_affordable_baskets_v3(10, items, lte=True)
    assert all(basket.cost <= 10 for basket in result)


def compare_results(items, basket_combinations):
    assert list(
        get_affordable_baskets(10, baskets_combinations, lte=True)
    ) == get_affordable_baskets_v3(10, items, lte=True)
