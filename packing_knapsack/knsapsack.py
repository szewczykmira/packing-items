from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    name: str
    weight: int
    value: int = 1

    def __str__(self):
        return self.name


@dataclass
class Knapsack:
    name: str
    weight: int
    value: int = 0

    def __str__(self):
        return self.name
