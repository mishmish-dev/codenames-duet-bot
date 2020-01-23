from telegram import Update
from telegram.ext import CallbackContext

from codenames.database import create_session_context
from codenames.database.models import User
from codenames.handlers.special_types import DeepLinkedCallbackQueryHandler
from codenames.handlers.special_types import LocalizedCommandHandler

from codenames.deep_linking import send_markup, language_options_markup, ChangeLanguagePayload


def show_options(update: Update, context: CallbackContext) -> None:
    send_markup(
        update,
        language_options_markup(context.language),
        context.language.t.CHOOSE_LANGUAGE
    )


def change_language(update: Update, context: CallbackContext) -> None:
    old_language = context.payload.language
    new_language = context.payload.new_language

    with create_session_context() as session:
        user = User.get_or_create(update.effective_user.id, session)
        user.language = new_language

    update.callback_query.edit_message_reply_markup(None)

    update.effective_chat.send_message(
        new_language.t.LANGUAGE_CHANGED
        + " " + old_language.t.RETURN_TO_LANGUAGE_CHOICE
    )


language_command_handler = LocalizedCommandHandler("language", show_options)
change_language_handler = DeepLinkedCallbackQueryHandler(change_language, payload_type=ChangeLanguagePayload)
