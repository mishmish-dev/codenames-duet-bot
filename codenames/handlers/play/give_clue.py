from telegram import Update
from telegram.ext import CallbackContext, Filters

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer
from codenames.handlers.special_types import LocalizedMessageHandler


GIVE_CLUE_REGEX = r"^(?P<clue>\D+)\s+(?P<agent_count>\d+)$"

def give_clue(update: Update, context: CallbackContext) -> None:
    clue = " ".join(context.match["clue"].split()).upper()
    agent_count = int(context.match["agent_count"])

    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            game = player.game

            if (len(game.team_listing(player.team.opposed())) == 0):
                update.effective_user.send_message(context.language.t.NOT_GIVING_CLUE_WAIT_FOR_OTHER_TEAM)

            elif game.give_clue(player.team):
                for other_player in game.players:
                    if other_player.id == player.id:
                        update.effective_user.send_message(
                            player.language.t.CLUE_ACCEPTED
                        )
                    else:
                        context.bot.send_message(
                            other_player.id,
                            other_player.language.tf.PLAYER_GIVES_CLUE(
                                nickname=player.nickname,
                                clue=clue,
                                agent_count=agent_count
                            )
                        )
            else:
                update.effective_user.send_message(context.language.t.NOT_YOUR_TURN_TO_GIVE_CLUE)
        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


give_clue_handler = LocalizedMessageHandler(Filters.regex(GIVE_CLUE_REGEX), give_clue)
