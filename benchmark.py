import timeit

from packing import filter_baskets, lazy, naive, with_itertools
from packing.basket import Item
from tabulate import tabulate

items = [
    Item(1),
    Item(2),
    Item(3),
    Item(4),
    Item(5),
]


HEADERS = [
    "Name",
    "Create combinations",
    "Create combinations and filter out affodable",
]
naive_implementation = [
    "Naive",
    timeit.timeit(lambda: naive.create_all(items), number=3000),
    timeit.timeit(
        lambda: filter_baskets.get_affordable_baskets(10, naive.create_all(items)),
        number=3000,
    ),
]
with_itertools = [  # type: ignore
    "Used itertools to generate combinations",
    timeit.timeit(lambda: with_itertools.create_all(items), number=3000),
    timeit.timeit(
        lambda: filter_baskets.get_affordable_baskets(
            10, with_itertools.create_all(items)
        ),
        number=3000,
    ),
]
lazy = [  # type: ignore
    "Lazy implementation",
    "----",
    timeit.timeit(lambda: lazy.get_affordable_baskets(10, items), number=3000),
]
table = tabulate([naive_implementation, with_itertools, lazy], headers=HEADERS)  # type: ignore
print(table)
