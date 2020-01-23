import pytest

from codenames.database.models.column_array import ColumnArray


class Sack:
    zombies = ColumnArray("zombie", 0, None)
    candies = ColumnArray("candy", 100, None)

    def __init__(self):
        for attr in type(self).__dict__.values():
            if isinstance(attr, ColumnArray):
                setattr(self, attr.len_column_name, None)


@pytest.fixture
def empty_sack():
    return Sack()


def test_operations(empty_sack):
    assert len(empty_sack.zombies) == 0
    assert len(empty_sack.candies) == 0

    empty_sack.candies.append("Sweet")
    assert len(empty_sack.candies) == 1

    empty_sack.candies.extend(("Bitter", "Banana", "Choco"))
    assert len(empty_sack.candies) == 4

    empty_sack.candies.insert(3, "Lemon")
    assert tuple(empty_sack.candies) == ("Sweet", "Bitter", "Banana", "Lemon", "Choco")

    empty_sack.candies.remove("Bitter")

    assert tuple(empty_sack.candies) == ("Sweet", "Banana", "Lemon", "Choco")


def test_max_len(empty_sack):
    with pytest.raises(IndexError):
        empty_sack.zombies.append("Brrrrrrrainsucker")

def test_max_len_2(empty_sack):
    with pytest.raises(IndexError):
        for _ in range(101):
            empty_sack.candies.append("M&M")
