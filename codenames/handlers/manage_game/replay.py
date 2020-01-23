from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer

from codenames.duet import Phase
from codenames.duet.render import render_board


def replay(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            game = player.game

            if game.phase in (Phase.VICTORY, Phase.DEFEAT):
                game.initialize_board()

                for other_player in game.players:
                    context.bot.send_photo(
                        other_player.id,
                        render_board(game, other_player.team),
                        other_player.language.tf.REPLAY(player.nickname)
                    )
        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


replay_handler = CommandHandler("replay", replay)
