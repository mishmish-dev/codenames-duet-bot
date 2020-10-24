from enum import Enum, auto

from codenames.utils import enum_exponent


class Team(Enum):
    FIRST = auto()
    SECOND = auto()

    def opposed(self) -> "Team":
        if self == Team.FIRST:
            return Team.SECOND

        return Team.FIRST

    def icon(self) -> str:
        if self == Team.FIRST:
            return "☝🏻"

        return "✌🏻"


class Identity(Enum):
    AGENT = auto()
    ASSASSIN = auto()
    BYSTANDER = auto()


class _IdentityPairMixin:
    def __getitem__(self, key) -> "IdentityPair":
        if isinstance(key, Team):
            if key == Team.FIRST:
                return self.value[0]
            if key == Team.SECOND:
                return self.value[1]

        raise KeyError(key)

IdentityPair = enum_exponent("IdentityPair", Identity, 2, type=_IdentityPairMixin)
