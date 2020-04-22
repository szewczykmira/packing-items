import timeit

from packing import filter_baskets, itertools, lazy, naive
from packing.basket import Item
from termcolor import colored

items = [
    Item(1),
    Item(2),
    Item(3),
    Item(4),
    Item(5),
]

print(colored("Most naive version of solution", "yellow"))
comb_v1 = lambda: naive.create_all(items)
affordable_combinations_v1 = lambda: filter_baskets.get_affordable_baskets(
    10, naive.create_all(items)
)
print(
    colored(
        "\t generating all combinations: {}".format(
            timeit.timeit(comb_v1, number=3000)
        ),
        "yellow",
    )
)
print(
    colored(
        "\t generating all combinations and filtering relevant one: {}\n".format(
            timeit.timeit(affordable_combinations_v1, number=3000,)
        ),
        "yellow",
    )
)


print(colored("Implementation using itertools", "white"))
comb_v2 = lambda: itertools.create_all(items)
affordable_combinations_v2 = lambda: filter_baskets.get_affordable_baskets(
    10, itertools.create_all(items)
)

print(
    colored(
        "\t Generating all combinations: {}".format(timeit.timeit(comb_v2, number=3000))
    ),
    "white",
)
print(
    colored(
        "\t Generating all combinations and filtering relevant one: {}".format(
            timeit.timeit(affordable_combinations_v2, number=3000)
        ),
        "white",
    )
)

print(colored("Lazy implementation", "red"))
affordable_combinations_v3 = lambda: lazy.get_affordable_baskets(10, items)
print(
    colored(
        "\t Generating all combinations and filtering relevant one: {}".format(
            timeit.timeit(affordable_combinations_v3, number=3000)
        ),
        "red",
    )
)
