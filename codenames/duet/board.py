from typing import Iterator, Optional, Sequence, Set, Tuple

from codenames.utils import AlphabeticComparisonMap

from codenames.duet.basic import Identity, IdentityPair, Team


BOARD_SIZE = 25
MAX_GUESS_COUNT = 26
MAX_CLUE_COUNT = 11
AGENT_COUNT_FOR_ONE_TEAM = 9

IDENTITY_PAIRS = (
    [(IdentityPair.ASSASSIN_ASSASSIN)]
    + [(IdentityPair.ASSASSIN_AGENT)]
    + [(IdentityPair.AGENT_ASSASSIN)]
    + [(IdentityPair.ASSASSIN_BYSTANDER)]
    + [(IdentityPair.BYSTANDER_ASSASSIN)]
    + [(IdentityPair.AGENT_AGENT)] * 3
    + [(IdentityPair.AGENT_BYSTANDER)] * 5
    + [(IdentityPair.BYSTANDER_AGENT)] * 5
    + [(IdentityPair.BYSTANDER_BYSTANDER)] * 7
)


class BoardMixin:
    def get_identity(self, position: int, for_team: Team) -> IdentityPair:
        return self.identity_pairs[position][for_team]

    def get_guess_history(self) -> Iterator[Tuple[int, Team, Identity]]:
        for position, team in zip(self.guess_positions, self.guess_teams):
            yield position, team, self.get_identity(position, team)

    def get_clue_history(self) -> Iterator[Tuple[str, Team]]:
        for clue, team in zip(self.clues, self.clue_teams):
            yield clue, team

    def clear_clue_history(self) -> None:
        self.clues.clear()
        self.clue_teams.clear()

    def clear_guess_history(self) -> None:
        self.guess_positions.clear()
        self.guess_teams.clear()

    def all_agents_found(self, for_team: Optional[Team] = None) -> bool:
        if for_team is None:
            return all(self.all_agents_found(team) for team in Team)

        agents_found = sum(
            1 for pos, _, identity in self.get_guess_history()
            if identity == Identity.AGENT and self.get_identity(pos, for_team) == Identity.AGENT
        )

        return agents_found == AGENT_COUNT_FOR_ONE_TEAM

    def available_guesses(self, for_team: Team) -> AlphabeticComparisonMap[int]:
        unavailable: Set[int] = set()
        for position, team, identity in self.get_guess_history():
            if team == for_team or identity != Identity.BYSTANDER:
                unavailable.add(position)

        return AlphabeticComparisonMap(
            (word, position)
            for position, word in enumerate(self.words)
            if position not in unavailable
        )

    def guess_identity(self, guess: str, team: Team) -> Optional[Identity]:
        position = self.available_guesses(team).get(guess)

        if position is None:
            return None

        self.guess_positions.append(position)
        self.guess_teams.append(team)

        return self.get_identity(position, team)
