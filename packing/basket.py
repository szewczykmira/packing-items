from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    price: int
    name: str = ""

    def __str__(self):
        return f"{self.name} - {self.price}"


@dataclass
class Basket:
    cost: int = 0
    items: List[Item] = field(default_factory=list)

    def __lshift__(self, other: Item):
        # usage self << Item
        self.items.append(other)
        self.cost += other.price
