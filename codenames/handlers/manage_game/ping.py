from telegram import Update
from telegram.ext import CallbackContext

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer

from codenames.duet import Phase
from codenames.duet.render import render_board

from codenames.handlers.special_types import LocalizedCommandHandler


def ping(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            game = player.game
            playing_team = game.playing_team
            phase = game.phase

            update.effective_user.send_message(context.language.t.REMINDER_SENT)

            if playing_team is None and phase == Phase.CLUE:
                for other_player in game.players:
                    reminder_message = other_player.language.tf.USERNAME_REMINDS(player.nickname) + "\n\n"
                    context.bot.send_message(
                        other_player.id,
                        other_player.language.tf.USERNAME_REMINDS(player.nickname)+ "\n\n"
                        + other_player.language.t.ANYONE_CAN_GIVE_CLUE
                    )

            elif phase == Phase.SUDDEN_DEATH:
                for other_player in game.players:
                    context.bot.send_message(
                        other_player.id,
                        other_player.language.tf.USERNAME_REMINDS(player.nickname)+ "\n\n"
                        + other_player.language.t.ALL_MAKE_GUESS_SUDDEN_DEATH
                    )

            elif phase in (Phase.VICTORY, Phase.DEFEAT):
                for other_player in game.players:
                    context.bot.send_message(
                        other_player.id,
                        other_player.language.tf.USERNAME_REMINDS(player.nickname)+ "\n\n"
                        + other_player.language.t.GAME_IS_OVER_REPLAY
                    )

            else:
                for other_player in game.team_listing(playing_team):
                    if phase == Phase.CLUE:
                        context.bot.send_message(
                            other_player.id,
                            other_player.language.tf.USERNAME_REMINDS(player.nickname)+ "\n\n"
                            + other_player.language.t.YOU_NOW_GIVE_CLUE
                        )
                    elif phase == Phase.GUESS_CANNOT_SKIP:
                        context.bot.send_message(
                            other_player.id,
                            other_player.language.tf.USERNAME_REMINDS(player.nickname)+ "\n\n"
                            + other_player.language.t.YOU_NOW_MAKE_GUESS_CANNOT_SKIP
                        )
                    elif phase == Phase.GUESS:
                        context.bot.send_message(
                            other_player.id,
                            other_player.language.tf.USERNAME_REMINDS(player.nickname)+ "\n\n"
                            + other_player.language.t.YOU_NOW_MAKE_GUESS
                        )

        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


ping_handler = LocalizedCommandHandler("ping", ping)
