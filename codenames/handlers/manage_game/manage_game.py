from random import sample
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import CallbackContext, CallbackQueryHandler

from codenames.duet import Team, pick_team, BOARD_SIZE, render_board
from codenames.database import create_session_context
from codenames.database.models import User, DuetPlayer, DuetGame
from codenames.resources import WORDLISTS

from codenames.handlers.special_types import LocalizedCommandHandler, LocalizedInlineQueryHandler
from codenames.handlers.special_types import DeepLinkedCallbackQueryHandler, DeepLinkedStartCommandHandler

from codenames.deep_linking import settings_markup, join_game_markup, DEFAULT_GAME_SETTINGS
from codenames.deep_linking import PrepareGamePayload, CreateGamePayload, JoinGamePayload

from codenames.handlers.manage_game.invite import invitation


INLINE_QUERY_RESULT_ID = "create"


def answer_inline_query(update: Update, context: CallbackContext) -> None:
    update.inline_query.answer(
        [
            InlineQueryResultArticle(
                id=INLINE_QUERY_RESULT_ID,
                title=context.language.t.CREATE_GAME_INLINE,
                input_message_content=InputTextMessageContent(
                    context.language.t.CHOOSE_NEW_GAME_SETTINGS
                ),
                reply_markup=settings_markup(DEFAULT_GAME_SETTINGS, context.language)
            )
        ],
        cache_time=0,
        is_personal=True
    )


def answer_new_game_command(update: Update, context: CallbackContext) -> None:
    update.effective_user.send_message(
        context.language.t.CHOOSE_NEW_GAME_SETTINGS,
        reply_markup=settings_markup(DEFAULT_GAME_SETTINGS, context.language)
    )


def prepare_game(update: Update, context: CallbackContext) -> None:
    update.callback_query.edit_message_reply_markup(
        settings_markup(context.payload, context.language)
    )


def create_game(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        user = User.get_or_create(update.effective_user.id, session)

        if user.player is None:
            user.player = DuetPlayer(
                team=Team.FIRST,
                nickname=user.nickname or update.effective_user.first_name
            )
            user.player.game = DuetGame(
                id=uuid4(),
                total_token_count=context.payload.token_count,
                wordlist_code=context.payload.wordlist_code
            )

            game = user.player.game
            game.initialize_board()

            text, reply_markup = invitation(
                user_id=update.effective_user.id,
                bot_username=context.bot.name[1:],
                language=context.language,
                session=session
            )

            update.callback_query.edit_message_text(context.language.t.GAME_CREATED + "\n\n" + text)
            update.callback_query.edit_message_reply_markup(reply_markup)

            update.effective_user.send_photo(render_board(game, Team.FIRST))

        else:
            update.effective_user.send_message(user.language.t.ALREADY_IN_GAME)


def join_game(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        user = User.get_or_create(update.effective_user.id, session)

        if user.player is None:
            game = session.query(DuetGame).get(context.payload.game_id)
            if game is None:
                return

            team = context.payload.team or pick_team(game)
            user.player = DuetPlayer(
                team=team,
                nickname=user.nickname or update.effective_user.first_name
            )
            user.player.game = game

            update.effective_user.send_photo(render_board(game, team))

        elif user.player.game_id != context.payload.game_id:
            update.effective_user.send_message(user.language.t.ALREADY_IN_GAME)


def leave_game(update: Update, context: CallbackContext) -> None:
    with create_session_context() as session:
        player = session.query(DuetPlayer).get(update.effective_user.id)

        if player is not None:
            game = player.game
            session.delete(player)
            if len(game.players) == 0:
                session.delete(game)

            update.effective_user.send_message(context.language.t.LEFT_GAME)
        else:
            update.effective_user.send_message(context.language.t.YOU_ARE_NOT_IN_GAME)


inline_query_handler = LocalizedInlineQueryHandler(answer_inline_query)
new_game_handler = LocalizedCommandHandler("new_game", answer_new_game_command)
leave_game_handler = LocalizedCommandHandler("leave_game", leave_game)

change_game_settings_handler = DeepLinkedCallbackQueryHandler(prepare_game, payload_type=PrepareGamePayload)
create_game_handler = DeepLinkedCallbackQueryHandler(create_game, payload_type=CreateGamePayload)
join_game_handler = DeepLinkedStartCommandHandler(join_game, payload_type=JoinGamePayload)
