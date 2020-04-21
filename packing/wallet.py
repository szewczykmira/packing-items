from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    name: str
    price: int

    def __str__(self):
        return self.name


@dataclass
class Basket:
    cost: int
    items: List[Item] = field(default_factory=list)
