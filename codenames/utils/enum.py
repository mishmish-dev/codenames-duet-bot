from enum import Enum, EnumMeta
from itertools import product


class StringEnum(str, Enum):
    pass


def enum_product(name: str, *enums: EnumMeta, separator="_", **kwargs) -> EnumMeta:
    return Enum(
        name,
        {
            separator.join(elem.name for elem in prod): tuple(prod)
            for prod in product(*enums)
        },
        **kwargs
    )

def enum_exponent(name: str, enum: EnumMeta, exponent: int, separator="_", **kwargs) -> EnumMeta:
    return enum_product(name, *(enum for _ in range(exponent)), separator=separator, **kwargs)
