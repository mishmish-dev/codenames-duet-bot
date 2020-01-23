import os.path
from typing import List, NamedTuple

from codenames.utils import AlphabeticComparisonSet


def load_wordlist(path: str) -> List[str]:
    with open(path) as words_file:
        return list(AlphabeticComparisonSet(line.strip() for line in words_file))


class NamedWordlist(NamedTuple):
    name: str
    wordlist: List[str]


WORDLISTS: List[NamedWordlist] = [
    NamedWordlist("🇷🇺 ориг.", load_wordlist("resources/wordlists/ru/original.txt")),
    NamedWordlist("🇷🇺 Дуэт", load_wordlist("resources/wordlists/ru/duet.txt")),
    NamedWordlist("🇷🇺 18+", load_wordlist("resources/wordlists/ru/deep_undercover.txt")),

    NamedWordlist("🇬🇧 orig.", load_wordlist("resources/wordlists/en/original.txt")),
    NamedWordlist("🇬🇧 Duet", load_wordlist("resources/wordlists/en/duet.txt")),
    NamedWordlist("🇬🇧 18+", load_wordlist("resources/wordlists/en/deep_undercover.txt"))
]
