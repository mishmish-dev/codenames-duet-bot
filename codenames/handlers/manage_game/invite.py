from typing import Optional, Tuple

from sqlalchemy.orm import Session
from telegram import Update
from telegram.ext import CallbackContext

from codenames.database import create_session_context
from codenames.database.models import DuetPlayer
from codenames.duet import Team
from codenames.i18n import Language
from codenames.handlers.special_types import LocalizedCommandHandler
from codenames.deep_linking import join_game_markup


def invitation(user_id: int, bot_username: str, language: Language, session: Session) -> Optional[Tuple]:
    player = session.query(DuetPlayer).get(user_id)

    if player is not None:
        game = player.game

        text = language.tf.INVITATION(
            first_team=language.conjunct(
                game.team_listing(Team.FIRST),
                language.t.NOBODY
            ),
            second_team=language.conjunct(
                game.team_listing(Team.SECOND),
                language.t.NOBODY
            ),
        )
        reply_markup = join_game_markup(
            bot_username=bot_username,
            game_id=game.id,
            language=language
        )

        return text, reply_markup


def invite(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        result = invitation(
            user_id=update.effective_user.id,
            bot_username=context.bot.name[1:],
            language=context.language,
            session=session
        )

    if result:
        text, reply_markup = result
        update.effective_user.send_message(text, reply_markup=reply_markup)
    else:
        update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


invite_handler = LocalizedCommandHandler("invite", invite)
