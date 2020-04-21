import timeit

from packing import combinations_v1, combinations_v2
from packing.basket import Item

if __name__ == "__main__":

    items = [
        Item(1),
        Item(2),
        Item(3),
        Item(4),
        Item(5),
    ]

    print(timeit.timeit(lambda: combinations_v1.create_all(items), number=3000))
    print(timeit.timeit(lambda: combinations_v2.create_all(items), number=3000))
