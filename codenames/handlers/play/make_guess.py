from telegram import Update
from telegram.ext import CallbackContext, Filters

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer
from codenames.duet import Identity, Phase
from codenames.duet.render import render_board
from codenames.handlers.special_types import LocalizedMessageHandler
from codenames.resources.reactions import VICTORY_STICKER_ID, DEFEAT_STICKER_ID


MAKE_GUESS_REGEX = r"^(?P<guess>\D+)$"

def make_guess(update: Update, context: CallbackContext) -> None:
    guess = " ".join(context.match["guess"].split()).upper()

    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            game = player.game

            if not game.is_correct_phase_to_make_guess(player.team):
                update.effective_user.send_message(context.language.t.NOT_YOUR_TURN_TO_MAKE_GUESS)
                return

            identity = game.make_guess(guess, player.team)

            if identity:
                all_agents_from_one_team_found = game.all_agents_found(player.team) and game.phase != Phase.VICTORY

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

                    if all_agents_from_one_team_found:
                        caption += "\n\n"
                        caption += other_player.language.t.ALL_AGENTS_FROM_ONE_TEAM_FOUND

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
                update.effective_user.send_message(context.language.t.UNKNOWN_CODENAME)

        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


make_guess_handler = LocalizedMessageHandler(Filters.regex(MAKE_GUESS_REGEX), make_guess)
