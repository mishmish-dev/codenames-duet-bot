from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from codenames.database import create_session_context
from codenames.database.models import User


def show_current_settings(update: Update, context: CallbackContext) -> None:
    user = User.get_or_create(update.effective_user.id)
    nickname = user.nickname
    language = user.language

    if nickname is None:
        nickname = language.tf.NICKNAME_DEFAULT_SETTING(
            update.effective_user.first_name
        )

    update.effective_chat.send_message(language.tf.CURRENT_SETTINGS(
        nickname=nickname,
        language=language.t.LANGUAGE_NAME
    ))


settings_handler = CommandHandler("settings", show_current_settings)
