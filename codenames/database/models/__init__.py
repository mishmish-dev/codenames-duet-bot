from typing import List

from sqlalchemy import BigInteger, Column, SmallInteger, Enum, String, Text, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy_utils import UUIDType, force_instant_defaults

from codenames.utils import to_snake_case_and_plural

from codenames import duet
from codenames.i18n import Language, DEFAULT_LANGUAGE

from codenames.database.models.base_model import BaseModel, ColumnArray


MAX_NICKNAME_LENGTH = 32
MAX_WORD_LENGTH = 22
MAX_CLUE_LENGTH = 40


class User(BaseModel):
    id = Column(BigInteger, primary_key=True)
    language = Column(Enum(Language), nullable=False, default=DEFAULT_LANGUAGE)
    nickname = Column(String(MAX_NICKNAME_LENGTH))

    player = relationship(
        "DuetPlayer",
        cascade="save-update, merge, delete",
        uselist=False,
        back_populates="user"
    )

force_instant_defaults(User)


class DuetPlayer(BaseModel):
    id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    nickname = Column(String(MAX_NICKNAME_LENGTH), nullable=False)
    game_id = Column(UUIDType, ForeignKey("duet_games.id"), nullable=False)
    team = Column(Enum(duet.Team), nullable=False)

    user = relationship("User", lazy="joined", back_populates="player")
    game = relationship("DuetGame", back_populates="players")

    @validates("nickname")
    def trim_nickname(self, key, nickname: str) -> str:
        return nickname[:MAX_NICKNAME_LENGTH]

    @property
    def language(self) -> Language:
        return self.user.language

    def __str__(self) -> str:
        return self.nickname


class DuetGame(duet.GameMixin, BaseModel):
    id = Column(UUIDType, primary_key=True)
    total_token_count = Column(SmallInteger, nullable=False)
    wordlist_code = Column(SmallInteger, nullable=False)

    phase = Column(Enum(duet.Phase), nullable=False, default=duet.Phase.CLUE)
    playing_team = Column(Enum(duet.Team))
    free_token_count = Column(SmallInteger)

    words = ColumnArray("word", duet.BOARD_SIZE, String(MAX_WORD_LENGTH))
    identity_pairs = ColumnArray("identity_pair", duet.BOARD_SIZE, Enum(duet.IdentityPair))
    clues = ColumnArray("clue", duet.MAX_CLUE_COUNT, Text)
    clue_teams = ColumnArray("clue_team", duet.MAX_CLUE_COUNT, Enum(duet.Team))
    guess_positions = ColumnArray("guess_position", duet.MAX_GUESS_COUNT, SmallInteger)
    guess_teams = ColumnArray("guess_team", duet.MAX_GUESS_COUNT, Enum(duet.Team))

    players = relationship("DuetPlayer", cascade="all, delete-orphan", back_populates="game")

    def team_listing(self, team: duet.Team) -> List[DuetPlayer]:
        return [player for player in self.players if player.team == team]
