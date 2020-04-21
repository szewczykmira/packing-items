import pytest

from ..basket import Item


@pytest.fixture
def items():
    return [
        Item(1),
        Item(2),
        Item(3),
        Item(4),
        Item(5),
    ]
