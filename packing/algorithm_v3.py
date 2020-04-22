from itertools import chain, combinations
from operator import eq, le
from typing import List

from .basket import Basket, Item


def get_affordable_baskets(value: int, items: List[Item], lte: bool = False):
    affodable_baskets = []
    op = le if lte else eq
    for basket_items in chain.from_iterable(
        [combinations(items, i) for i in range(1, len(items) + 1)]
    ):
        items_list = list(basket_items)
        basket_cost = sum([item.price for item in items_list])
        if op(basket_cost, value):
            affodable_baskets.append(Basket(cost=basket_cost, items=items_list))
    return affodable_baskets
