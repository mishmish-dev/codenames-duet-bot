from codenames.database import create_session_context
from codenames.database.models import User, MAX_NICKNAME_LENGTH
from codenames.handlers.special_types import LocalizedCommandHandler, LocalizedMessageHandler
from enum import IntEnum, auto
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler, Filters


class State(IntEnum):
    END = ConversationHandler.END
    TYPING_NICKNAME = auto()


def command_nickname(update: Update, context: CallbackContext) -> State:
    with create_session_context() as session:
        user = User.get_or_create(update.effective_user.id, session)
        nickname = user.nickname

    if nickname is None:
        update.effective_chat.send_message(context.language.t.CHANGE_NICKNAME_FROM_NOT_SET)
    else:
        update.effective_chat.send_message(
            context.language.tf.CHANGE_NICKNAME_FROM_SET(nickname)
        )

    return State.TYPING_NICKNAME


def type_nickname(update: Update, context: CallbackContext) -> State:
    nickname = " ".join(update.message.text.split())
    if len(nickname) > MAX_NICKNAME_LENGTH:
        update.effective_chat.send_message(
            context.language.tf.NICKNAME_TOO_LONG(MAX_NICKNAME_LENGTH)
        )
        return State.TYPING_NICKNAME

    with create_session_context() as session:
        user = User.get_or_create(update.effective_user.id, session)
        user.nickname = nickname

    update.effective_chat.send_message(context.language.t.SUCCESS)
    return State.END


def clear(update: Update, context: CallbackContext) -> State:
    with create_session_context() as session:
        user = User.get_or_create(update.effective_user.id, session)
        user.nickname = None

    update.effective_chat.send_message(context.language.t.NICKNAME_CLEARED)
    return State.END


def cancel(update: Update, context: CallbackContext) -> State:
    update.effective_chat.send_message(context.language.t.CANCELLED)
    return State.END


def fallback(update: Update, context: CallbackContext) -> None:
    update.effective_chat.send_message(context.language.t.DONT_UNDERSTAND)


nickname_handler = ConversationHandler(
    entry_points=[
        LocalizedCommandHandler("nickname", command_nickname),
    ],
    states={
        State.TYPING_NICKNAME: [
            LocalizedCommandHandler("clear", clear),
            LocalizedMessageHandler(Filters.text, type_nickname),
        ],
    },
    fallbacks=[
        LocalizedCommandHandler("cancel", cancel),
        LocalizedMessageHandler(Filters.all, fallback),
    ],
    allow_reentry=True
)
