from operator import itemgetter
from typing import Callable

from codenames.i18n import phrases
from codenames.i18n.language import _Language


DEFAULT_LANGUAGE = _Language.RUSSIAN
FALLBACK_LANGUAGE = _Language.ENGLISH

class Translation:
    def __init__(self, language: _Language) -> None:
        self._itemgetter = itemgetter(language)
        self._fallback_itemgetter = itemgetter(FALLBACK_LANGUAGE)

    def __getattr__(self, name: str) -> str:
        phrases_dict = getattr(phrases, name)

        try:
            return self._itemgetter(phrases_dict)
        except KeyError:
            return self._fallback_itemgetter(phrases_dict)


class TranslationFormat(Translation):
    def __getattr__(self, name: str) -> Callable:
        template = super().__getattr__(name)

        def formatter(*args, **kwargs) -> str:
            return template.format(*args, **kwargs)

        return formatter


for language in _Language:
    language.t = Translation(language)
    language.tf = TranslationFormat(language)


Language = _Language
