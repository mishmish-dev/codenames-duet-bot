from uuid import UUID

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from codenames.utils import CycleDirection

from codenames.deep_linking.payload import Payload, GameSettings, ChangeLanguagePayload
from codenames.deep_linking.payload import PrepareGamePayload, CreateGamePayload, JoinGamePayload
from codenames.deep_linking.payload import cycle_token_count, cycle_wordlist_code
from codenames.duet import Team
from codenames.i18n import Language
from codenames.resources.wordlists import WORDLISTS


ARROW_TEMPLATES = {
    CycleDirection.LEFT: "⬅️ :: {}",
    CycleDirection.RIGHT: "{} :: ➡️"
}


def callback_button(text: str, payload: Payload) -> InlineKeyboardButton:
    return InlineKeyboardButton(text, callback_data=str(payload))

def start_url_button(text: str, bot_username: str, payload: Payload) -> InlineKeyboardButton:
    return InlineKeyboardButton(text, url=f"https://t.me/{bot_username}?start={payload}")


def send_markup(update: Update, markup: InlineKeyboardMarkup, message: str) -> None:
    if update.callback_query:
        update.callback_query.edit_message_reply_markup(markup)

    elif update.effective_user:
        update.effective_user.send_message(message, reply_markup=markup)


def prepare_game_button(text: str, settings: GameSettings, language: Language) -> InlineKeyboardButton:
    return callback_button(
        text,
        PrepareGamePayload(
            language=language,
            token_count=settings.token_count,
            wordlist_code=settings.wordlist_code
        )
    )

def cycle_token_count_button(direction: CycleDirection, settings: GameSettings, language: Language) -> InlineKeyboardButton:
    return prepare_game_button(
        text=ARROW_TEMPLATES[direction].format(language.tf.TOKEN_COUNT_SETTING(settings.token_count)),
        settings=settings,
        language=language
    )

def cycle_wordlist_code_button(direction: CycleDirection, settings: GameSettings, language: Language) -> InlineKeyboardButton:
    return prepare_game_button(
        text=ARROW_TEMPLATES[direction].format(WORDLISTS[settings.wordlist_code].name),
        settings=settings,
        language=language
    )


def settings_markup(settings: GameSettings, language: Language) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            cycle_token_count_button(
                direction=direction,
                settings=cycle_token_count(direction, settings),
                language=language
            )
            for direction in CycleDirection
        ],
        [
            cycle_wordlist_code_button(
                direction=direction,
                settings=cycle_wordlist_code(direction, settings),
                language=language
            )
            for direction in CycleDirection
        ],
        [
            callback_button(
                text=language.tf.CREATE_GAME_WITH_SETTINGS(
                    token_count=settings.token_count,
                    wordlist=WORDLISTS[settings.wordlist_code].name
                ),
                payload=CreateGamePayload(
                    language=language,
                    token_count=settings.token_count,
                    wordlist_code=settings.wordlist_code
                )
            )
        ]
    ])


def join_game_markup(bot_username: str, game_id: UUID, language: Language) -> InlineKeyboardMarkup:
    team_texts = [language.t.JOIN_GAME_FIRST_TEAM, language.t.JOIN_GAME_SECOND_TEAM]

    return InlineKeyboardMarkup([
        [
            start_url_button(
                text=language.t.JOIN_GAME_AUTO_TEAM,
                bot_username=bot_username,
                payload=JoinGamePayload(game_id=game_id, language=language)
            )
        ],
        [
            start_url_button(
                text=text,
                bot_username=bot_username,
                payload=JoinGamePayload(game_id=game_id, language=language, team=team)
            )
            for team, text in zip(Team, team_texts)
        ]
    ])


def language_options_markup(language: Language) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup.from_column([
        callback_button(
            language_option.t.LANGUAGE_NAME,
            ChangeLanguagePayload(
                language=language,
                new_language=language_option
            )
        )
        for language_option in Language
    ])
