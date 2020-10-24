from telegram import Update
from telegram.ext import CallbackContext

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer
from codenames.handlers.special_types import LocalizedCommandHandler


def end_turn(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            game = player.game

            if game.end_turn(player.team):
                for other_player in game.players:
                    if other_player.id == player.id:
                        update.effective_user.send_message(
                            player.language.t.TURN_ENDED
                        )
                    else:
                        context.bot.send_message(
                            other_player.id,
                            other_player.language.tf.PLAYER_ENDED_TURN(
                                player.nickname
                            )
                        )
        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


end_turn_handler = LocalizedCommandHandler("end_turn", end_turn)
