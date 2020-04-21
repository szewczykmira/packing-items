import timeit

from packing.algorithm import (
    create_all_combinations,
    create_combinations_with_itertools,
)
from packing.basket import Item

if __name__ == "__main__":

    items = [
        Item(1),
        Item(2),
        Item(3),
        Item(4),
        Item(5),
    ]

    print(timeit.timeit(lambda: create_all_combinations(items), number=3000))
    print(timeit.timeit(lambda: create_combinations_with_itertools(items), number=3000))
