from argparse import ArgumentParser
from typing import Dict, Optional

from telegram.ext import Updater

from codenames.database import initialize as initialize_database
from codenames.handlers import HANDLERS


def get_updater(token: str) -> Updater:

    updater = Updater(token=token)

    for handler in HANDLERS:
        updater.dispatcher.add_handler(handler)

    return updater


def webhook(*,
    token: str,
    db: str,
    debug: bool,
    webhook_url: str,
    listen_address: str,
    listen_port: int
) -> None:

    updater = get_updater(token)
    initialize_database(db, echo_sql=debug)

    updater.start_webhook(
        listen=listen_address,
        port=listen_port,
        url_path=token,
        webhook_url=webhook_url,
    )

    updater.idle()


def long_polling(*,
    token: str,
    db: str,
    debug: bool
) -> None:

    updater = get_updater(token)
    initialize_database(db)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    import logging

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    parser = ArgumentParser(description=(
        "Long polling mode is default. "
        "To run bot in webhook mode, provide corresponding options."
    ))

    parser.add_argument("--token", required=True, help="Telegram Bot token")
    parser.add_argument("--db", required=True, help="database connection string")
    parser.add_argument("--debug", type=bool, default=False, help="Debug mode")
    parser.add_argument("--webhook-url", help="webhook URL")
    parser.add_argument("--listen-address", help="webhook server listen address")
    parser.add_argument("--listen-port", type=int, help="webhook server listen port")

    args = parser.parse_args()
    if (
        args.webhook_url is None and
        args.listen_address is None and
        args.listen_port is None
    ):
        long_polling(
            token=args.token,
            db=args.db,
            debug=args.debug,
        )
    elif (
        args.webhook_url is not None and
        args.listen_address is not None and
        args.listen_port is not None
    ):
        webhook(
            token=args.token,
            db=args.db,
            debug=args.debug,
            listen_address=args.listen_address,
            listen_port=args.listen_port,
            webhook_url=args.webhook_url,
        )
    else:
        parser.error(
            "All of '--webhook-url', '--listen-address' and '--listen-port' "
            "options is required for webhook mode."
        )
