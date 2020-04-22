from operator import eq, lt
from typing import Iterator, List

from packing.basket import Basket, Item


def get_affordable_baskets(
    value: int, baskets: List[Basket], lte: bool = False
) -> Iterator[Basket]:
    op = lt if lte else eq
    return filter(lambda x: op(x.cost, value), baskets)
