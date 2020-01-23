from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler


def retrieve_audio_id(update: Update, context: CallbackContext) -> None:
    id = update.effective_message.audio.file_id
    update.effective_user.send_message(id)


def retrieve_sticker_id(update: Update, context: CallbackContext) -> None:
    id = update.effective_message.sticker.file_id
    update.effective_user.send_message(id)


audio_handler = MessageHandler(Filters.audio, retrieve_audio_id)
sticker_handler = MessageHandler(Filters.sticker, retrieve_sticker_id)
