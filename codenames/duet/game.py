from enum import Enum, auto
from random import choice, sample
from typing import Optional

from codenames.duet.basic import Identity, IdentityPair, Team
from codenames.duet.board import BoardMixin, BOARD_SIZE, IDENTITY_PAIRS
from codenames.resources import WORDLISTS
from codenames.utils import AlphabeticComparisonSet


class Phase(Enum):
    CLUE = auto()
    GUESS_CANNOT_SKIP = auto()
    GUESS = auto()
    SUDDEN_DEATH = auto()
    VICTORY = auto()
    DEFEAT = auto()


class GameMixin(BoardMixin):
    def give_clue(self, clue: str, team: Team) -> bool:
        if not (self.phase == Phase.CLUE and self.playing_team in (team, None)):
            return False

        self.clues.append(clue)
        self.clue_teams.append(team)

        self.phase = Phase.GUESS_CANNOT_SKIP
        self.playing_team = team.opposed()

        return True

    def is_correct_phase_to_make_guess(self, team: Team) -> bool:
        return (
            (self.phase in (Phase.GUESS_CANNOT_SKIP, Phase.GUESS) and self.playing_team == team)
            or self.phase == Phase.SUDDEN_DEATH
        )

    def make_guess(self, guess: str, team: Team) -> Optional[Identity]:
        if not self.is_correct_phase_to_make_guess(team):
            return None

        identity = self.guess_identity(guess, team)
        if identity is None:
            return None

        if identity == Identity.ASSASSIN:
            self.phase = Phase.DEFEAT

        elif identity == Identity.AGENT:
            if self.all_agents_found():
                self.phase = Phase.VICTORY

            elif self.phase in (Phase.GUESS_CANNOT_SKIP, Phase.GUESS) and self.all_agents_found(team):
                self.end_turn(team, force=True)

            elif self.phase != Phase.SUDDEN_DEATH:
                self.phase = Phase.GUESS

        elif identity == Identity.BYSTANDER:
            if self.phase == Phase.SUDDEN_DEATH:
                self.phase = Phase.DEFEAT
            else:
                self.end_turn(team, force=True)

        return identity

    def end_turn(self, team: Team, force: bool = False) -> bool:
        if not (
            (self.phase == Phase.GUESS and team == self.playing_team)
            or force
        ):
            return False

        self.free_token_count -= 1
        if self.free_token_count == 0:
            self.phase = Phase.SUDDEN_DEATH
        else:
            self.phase = Phase.CLUE
            if self.all_agents_found(team.opposed()):
                self.playing_team = team.opposed()

        return True

    def initialize_board(self) -> None:
        self.clear_clue_history()
        self.clear_guess_history()
        self.free_token_count = self.total_token_count

        enough_many_words = sample(WORDLISTS[self.wordlist_code].wordlist, BOARD_SIZE * 2)
        previous_words = AlphabeticComparisonSet(self.words)
        words = (word for word in enough_many_words if word not in previous_words)
        identity_pairs = sample(IDENTITY_PAIRS, BOARD_SIZE)

        self.words.clear()
        self.identity_pairs.clear()

        for word, identities in zip(words, identity_pairs):
            self.words.append(word)
            self.identity_pairs.append(identities)

        self.phase = Phase.CLUE
        self.playing_team = None


def pick_team(game) -> Team:
    first_team_size = sum(1 for player in game.players if player.team == Team.FIRST)
    second_team_size = sum(1 for player in game.players if player.team == Team.SECOND)

    if first_team_size == second_team_size:
        return choice(Team)

    if first_team_size > second_team_size:
        return Team.SECOND

    return Team.FIRST
