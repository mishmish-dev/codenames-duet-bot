from telegram import Update
from telegram.ext import CallbackContext

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer
from codenames.handlers.special_types import LocalizedCommandHandler


def clue_history(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            clues = "\n".join((
                context.language.tf.CLUE_HISTORY_ITEM(team=team.icon(), clue=clue)
                for clue, team in player.game.get_clue_history()
            ))

            if clues != "":
                update.effective_user.send_message(context.language.tf.CLUE_HISTORY(clues))
            else:
                update.effective_user.send_message(context.language.t.CLUE_HISTORY_EMPTY)

        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


clue_history_handler = LocalizedCommandHandler("clue_history", clue_history)
