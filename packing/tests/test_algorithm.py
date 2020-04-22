import pytest

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
