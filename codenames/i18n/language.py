from enum import StrEnum
from typing import Iterable


class _Language(StrEnum):
    ENGLISH = "en"
    RUSSIAN = "ru"
    PERSIAN = "fa"

    def conjunct(self, items: Iterable, nothing: str) -> str:
        items = [str(item) for item in items]
        if len(items) == 0:
            return nothing
        elif len(items) == 1:
            return items[0]

        return ", ".join(items[:-1]) + " " + self.t.AND + " " + items[-1]
