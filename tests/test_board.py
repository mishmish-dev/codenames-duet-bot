import pytest
from codenames.duet import board as brd, Identity, IdentityPair, Team
from collections import defaultdict


COUNT_TEXT = ("one", "two", "three", "four", "five", "six", "seven")


class Board(brd.BoardMixin):
    def __init__(self):
        identity_pair_counts = defaultdict(int)

        self.words = []
        self.identity_pairs = brd.IDENTITY_PAIRS
        self.guess_positions = []
        self.guess_teams = []

        for identities in brd.IDENTITY_PAIRS:
            count = COUNT_TEXT[identity_pair_counts[identities]]
            identity_pair_counts[identities] += 1
            self.words.append(f"{identities.name} {count}")

    def get_guess_history(self):
        return list(super().get_guess_history())


@pytest.fixture
def board():
    return Board()


def test_guess(board):
    assert len(board.get_guess_history()) == 0

    assert board.guess_identity("Eliza", Team.FIRST) is None
    assert len(board.get_guess_history()) == 0

    assert board.guess_identity("agent agent one", Team.FIRST) == Identity.AGENT
    assert len(board.get_guess_history()) == 1
    assert board.guess_identity("agent agent one", Team.FIRST) is None
    assert len(board.get_guess_history()) == 1
    assert board.guess_identity("agent agent one", Team.SECOND) is None

    assert board.guess_identity("bystander-agent TWO", Team.SECOND) == Identity.AGENT
    assert len(board.get_guess_history()) == 2
    assert board.guess_identity("BystanderAgentTwo", Team.FIRST) is None
    assert len(board.get_guess_history()) == 2

    assert board.guess_identity("bYstandeR::Bystander three", Team.FIRST) == Identity.BYSTANDER
    assert len(board.get_guess_history()) == 3

    assert board.guess_identity("bystander bystander three", Team.FIRST) is None
    assert board.guess_identity("bystander bystander three", Team.SECOND) == Identity.BYSTANDER
    assert board.guess_identity("bystander bystander three", Team.SECOND) is None
    assert len(board.get_guess_history()) == 4

    assert board.guess_identity("assassin bystander one", Team.SECOND) == Identity.BYSTANDER
    assert board.guess_identity("assassin bystander one", Team.FIRST) == Identity.ASSASSIN
