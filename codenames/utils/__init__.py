import re
from enum import IntEnum
from typing import Callable, TypeVar

from codenames.utils.alphabetic_comparison import AlphabeticComparisonMap
from codenames.utils.alphabetic_comparison import AlphabeticComparisonSet
from codenames.utils.enum import enum_product, enum_exponent


_T = TypeVar("_T")

_all_capital_word = re.compile(r"([A-Z]+)([A-Z][a-z])")
_first_capital_word = re.compile(r"([a-z0-9])([A-Z])")
_underscore_substitution = r"\1_\2"


def to_snake_case_and_plural(string: str) -> str:
    string = _all_capital_word.sub(_underscore_substitution, string)
    string = _first_capital_word.sub(_underscore_substitution, string)
    return string.lower() + "s"


class CycleDirection(IntEnum):
    LEFT = -1
    RIGHT = 1

def cycle(direction: CycleDirection, num: int, min_num: int, max_num: int) -> int:
    new_num = num + direction

    if new_num < min_num:
        return max_num

    if new_num > max_num:
        return min_num

    return new_num
