import re
from typing import Optional, Type, TypeVar
from uuid import UUID

from codenames.utils import cycle, CycleDirection

from codenames.duet import Team
from codenames.i18n import Language
from codenames.resources.wordlists import WORDLISTS


MIN_TOKEN_COUNT = 6
MAX_TOKEN_COUNT = 11


PayloadType = TypeVar("PayloadType", bound="Payload")


class Payload:
    def __init__(self, language, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.language = Language(language)

    def __init_subclass__(cls, *args, **kwargs) -> None:
        super().__init_subclass__(*args, **kwargs)
        pattern = r"^" + cls.PREFIX + r"_(?P<language>[a-z]+)_" + cls.ARGS_REGEX + r"$"
        cls.FULL_REGEX = re.compile(pattern)

    @classmethod
    def parse(cls: Type[PayloadType], raw_payload: str) -> Optional[PayloadType]:
        match = cls.FULL_REGEX.match(raw_payload)

        if match is None:
            return None

        try:
            return cls(**match.groupdict())
        except ValueError:
            return None

    def __str__(self) -> str:
        return f"{self.PREFIX}_{self.language}_{self.dump_args()}"


class ChangeLanguagePayload(Payload):
    PREFIX = "lang"
    ARGS_REGEX = r"(?P<new_language>[a-z]+)"

    def __init__(self, new_language, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.new_language = Language(new_language)

    def dump_args(self) -> str:
        return f"{self.new_language}"


class JoinGamePayload(Payload):
    PREFIX = "join"
    ARGS_REGEX = r"(?P<game_id>[a-zA-Z0-9-]+)_(?P<team>\d)"

    def __init__(self, game_id, team=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.game_id = game_id if isinstance(game_id, UUID) else UUID(game_id)

        if team is None or isinstance(team, Team):
            self.team = team
        elif team == "0":
            self.team = None
        elif team == "1":
            self.team = Team.FIRST
        elif team == "2":
            self.team = Team.SECOND
        else:
            raise ValueError

    def dump_args(self) -> str:
        if self.team is None:
            team_str = "0"
        elif self.team == Team.FIRST:
            team_str = "1"
        elif self.team == Team.SECOND:
            team_str = "2"

        return f"{self.game_id.hex}_{team_str}"


class GameSettings:
    ARGS_REGEX = r"(?P<token_count>\d+)_(?P<wordlist_code>\d+)"

    def __init__(self, token_count, wordlist_code, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.token_count = int(token_count)
        self.wordlist_code = int(wordlist_code)

        if (
            self.token_count not in range(MIN_TOKEN_COUNT, MAX_TOKEN_COUNT + 1)
            or self.wordlist_code not in range(len(WORDLISTS))
        ):
            raise ValueError

    def dump_args(self) -> str:
        return f"{self.token_count}_{self.wordlist_code}"

DEFAULT_GAME_SETTINGS = GameSettings(8, 1) # 8 tokens, Russian Duet wordlist


def cycle_token_count(direction: CycleDirection, settings: GameSettings) -> GameSettings:
    new_token_count = cycle(direction, settings.token_count, MIN_TOKEN_COUNT, MAX_TOKEN_COUNT)
    return GameSettings(new_token_count, settings.wordlist_code)

def cycle_wordlist_code(direction: CycleDirection, settings: GameSettings) -> GameSettings:
    new_wordlist_code = cycle(direction, settings.wordlist_code, 0, len(WORDLISTS) - 1)
    return GameSettings(settings.token_count, new_wordlist_code)


class CreateGamePayload(Payload, GameSettings):
    PREFIX = "create"

class PrepareGamePayload(Payload, GameSettings):
    PREFIX = "settings"
