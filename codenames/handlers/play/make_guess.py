from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer
from codenames.duet import Identity, Phase
from codenames.duet.render import render_board
from codenames.resources.reactions import VICTORY_STICKER_ID, DEFEAT_STICKER_ID


MAKE_GUESS_REGEX = r"^(?P<guess>\D+)$"

def make_guess(update: Update, context: CallbackContext) -> None:
    guess = " ".join(context.match["guess"].split()).upper()

    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            game = player.game

            identity = game.make_guess(guess, player.team)

            if identity:
                for other_player in game.players:
                    if identity == Identity.AGENT:
                        bumped_into = other_player.language.t.BUMPED_INTO_AGENT
                    elif identity == Identity.BYSTANDER:
                        bumped_into = other_player.language.t.BUMPED_INTO_BYSTANDER
                    elif identity == Identity.ASSASSIN:
                        bumped_into = other_player.language.t.BUMPED_INTO_ASSASSIN

                    if other_player.id == player.id:
                        caption = bumped_into
                    else:
                        caption = other_player.language.tf.PLAYER_MAKES_GUESS(
                            nickname=player.nickname,
                            guess=guess,
                            result=bumped_into
                        )

                    context.bot.send_photo(
                        other_player.id,
                        render_board(game, other_player.team),
                        caption
                    )

                    if game.phase == Phase.VICTORY:
                        context.bot.send_sticker(
                            other_player.id,
                            VICTORY_STICKER_ID
                        )
                    elif game.phase == Phase.DEFEAT:
                        context.bot.send_sticker(
                            other_player.id,
                            DEFEAT_STICKER_ID
                        )
                    elif game.phase == Phase.SUDDEN_DEATH:
                        context.bot.send_message(
                            other_player.id,
                            other_player.language.t.SUDDEN_DEATH
                        )

        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


make_guess_handler = MessageHandler(Filters.regex(MAKE_GUESS_REGEX), make_guess)
