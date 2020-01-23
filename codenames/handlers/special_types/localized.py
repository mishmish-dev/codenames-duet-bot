from telegram.ext import CallbackQueryHandler, CommandHandler, InlineQueryHandler, MessageHandler

from codenames.database import create_session_context
from codenames.database.models import User


class Localized:
    def collect_additional_context(self, context, update, dispatcher, check_result) -> None:
        super().collect_additional_context(context, update, dispatcher, check_result)
        context.language = User.get_or_create(update.effective_user.id).language


class LocalizedCallbackQueryHandler(Localized, CallbackQueryHandler):
    pass

class LocalizedCommandHandler(Localized, CommandHandler):
    pass

class LocalizedInlineQueryHandler(Localized, InlineQueryHandler):
    pass

class LocalizedMessageHandler(Localized, MessageHandler):
    pass
