from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    price: int

    def __str__(self):
        return self.name
