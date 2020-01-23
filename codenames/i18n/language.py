from typing import Iterable

from codenames.utils import StringEnum


class _Language(StringEnum):
    ENGLISH = "en"
    RUSSIAN = "ru"

    def conjunct(self, items: Iterable, nothing: str) -> str:
        items = [str(item) for item in items]
        if len(items) == 0:
            return nothing
        elif len(items) == 1:
            return items[0]

        return ", ".join(items[:-1]) + " " + self.t.AND + " " + items[-1]
