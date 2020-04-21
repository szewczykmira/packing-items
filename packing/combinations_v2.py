"""
Implemenation that is taking advantage of itertools module.
"""
from itertools import combinations
from typing import List

from .basket import Basket, Item


def convert_to_baskets(combinations: List[List[Item]]) -> List[Basket]:
    baskets = []
    for combination in combinations:
        baskets.append(
            Basket(items=combination, cost=sum([item.price for item in combination]))
        )
    return baskets


def create_all(items: List[Item]) -> List[Basket]:
    all_combinations = []
    for i in range(1, len(items) + 1):
        all_combinations.extend(list(combinations(items, i)))

    return convert_to_baskets(all_combinations)  # type: ignore
