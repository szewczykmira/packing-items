"""
This is naive implementation of the algorithm. We add item to every previously generated basket and update it value.
"""

import copy
from typing import List

from .basket import Basket, Item


def create_combinations_with_item(item: Item, baskets: List[Basket]) -> List[Basket]:
    combinations = []
    for basket in baskets:
        basket_cp = copy.deepcopy(basket)
        basket_cp << item
        combinations.append(basket_cp)
    return combinations


def create_all(items: List[Item]) -> List[Basket]:
    empty_basket = Basket()
    combinations = [empty_basket]
    for item in items:
        combinations.extend(create_combinations_with_item(item, combinations))
    combinations.remove(empty_basket)
    return combinations
