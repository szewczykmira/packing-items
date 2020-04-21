import copy
from itertools import combinations
from typing import List

from .basket import Basket, Item


def create_combinations_with_item(item: Item, baskets: List[Basket]) -> List[Basket]:
    combinations = []
    for basket in baskets:
        basket_cp = copy.deepcopy(basket)
        basket_cp << item
        combinations.append(basket_cp)
    return combinations


def create_all_combinations(items: List[Item]) -> List[Basket]:
    empty_basket = Basket()
    combinations = [empty_basket]
    for item in items:
        combinations.extend(create_combinations_with_item(item, combinations))
    combinations.remove(empty_basket)
    return combinations


# Algorithm v 2.0 to check what options will be faster
def convert_to_baskets(combinations: List[List[Item]]) -> List[Basket]:
    baskets = []
    for combination in combinations:
        baskets.append(
            Basket(items=combination, cost=sum([item.price for item in combination]))
        )
    return baskets


def create_combinations_with_itertools(items: List[Item]) -> List[Basket]:
    all_combinations = []
    for i in range(1, len(items) + 1):
        all_combinations.extend(list(combinations(items, i)))

    return convert_to_baskets(all_combinations)
