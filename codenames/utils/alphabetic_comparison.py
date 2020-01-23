from typing import AbstractSet, Dict, Iterable, Mapping, Tuple, TypeVar, overload


def normalize(string: str) -> str:
    return "".join(filter(str.isalpha, string)).lower().replace("ё", "е")

class AlphabeticComparisonString(str):
    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return normalize(self) == normalize(other)

        return super().__eq__(other)

    def __hash__(self) -> int:
        return hash(normalize(self))


ValueType_co = TypeVar("ValueType_co", covariant=True)

class AlphabeticComparisonMap(Mapping[str, ValueType_co]):
    @overload
    def __init__(self, mapping: Mapping[str, ValueType_co]) -> None:
        ...

    @overload
    def __init__(self, mapping: Iterable[Tuple[str, ValueType_co]]) -> None:
        ...

    def __init__(self, mapping=()) -> None:
        if isinstance(mapping, Mapping):
            mapping = mapping.items()

        self._dict: Dict[AlphabeticComparisonString, ValueType_co] = {
            AlphabeticComparisonString(key): value for key, value in mapping
        }

    def __getitem__(self, key):
        return self._dict[AlphabeticComparisonString(key)]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)


class AlphabeticComparisonSet(AbstractSet[str]):
    def __init__(self, iterable: Iterable[str] = ()) -> None:
        self._set = set(AlphabeticComparisonString(item) for item in iterable)

    def __contains__(self, item):
        return AlphabeticComparisonString(item) in self._set

    def __iter__(self):
        return iter(self._set)

    def __len__(self):
        return len(self._set)
