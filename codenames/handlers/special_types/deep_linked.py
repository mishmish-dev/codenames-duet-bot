from telegram.ext import Handler, CallbackQueryHandler, CommandHandler


class DeepLinked:
    def __init__(self, *args, payload_type, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.payload_type = payload_type


class DeepLinkedCallbackQueryHandler(DeepLinked, CallbackQueryHandler):
    def check_update(self, update):
        if not super().check_update(update):
            return

        raw_payload = update.callback_query.data
        if raw_payload:
            return self.payload_type.parse(update.callback_query.data)

    def collect_additional_context(self, context, update, dispatcher, check_result) -> None:
        super().collect_additional_context(context, update, dispatcher, check_result)
        context.payload = check_result
        context.language = check_result.language

    def handle_update(self, update, *args, **kwargs):
        update.callback_query.answer()
        return super().handle_update(update, *args, **kwargs)


class DeepLinkedStartCommandHandler(DeepLinked, CommandHandler):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("start", *args, **kwargs)

    def check_update(self, update):
        check_result = super().check_update(update)
        if not check_result or not check_result[0]:
            return

        payload = self.payload_type.parse(check_result[0][0])
        if payload is None:
            return

        return (
            check_result,
            {"payload": payload, "language": payload.language}
        )
