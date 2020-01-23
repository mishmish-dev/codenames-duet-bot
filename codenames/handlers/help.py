from telegram import Update
from telegram.ext import CallbackContext

from codenames.handlers.special_types import LocalizedCommandHandler


def show_help(update: Update, context: CallbackContext) -> None:
    update.effective_chat.send_message(context.language.t.HELP_MESSAGE)


help_handler = LocalizedCommandHandler("help", show_help)
start_handler = LocalizedCommandHandler("start", show_help)
