from codenames.handlers.manage_game import inline_query_handler, new_game_handler
from codenames.handlers.manage_game import change_game_settings_handler, create_game_handler
from codenames.handlers.manage_game import join_game_handler, leave_game_handler
from codenames.handlers.manage_game import invite_handler, replay_handler

from codenames.handlers.play import give_clue_handler, make_guess_handler, end_turn_handler

from codenames.handlers.manage_settings import settings_handler, nickname_handler
from codenames.handlers.manage_settings import language_command_handler, change_language_handler

from codenames.handlers.help import help_handler, start_handler
from codenames.handlers.retrieve_id import audio_handler, sticker_handler


HANDLERS = [
    inline_query_handler,
    new_game_handler,
    change_game_settings_handler,
    create_game_handler,
    join_game_handler,
    invite_handler,
    replay_handler,
    leave_game_handler,

    settings_handler,
    nickname_handler,
    language_command_handler,
    change_language_handler,

    help_handler,

    # this should be after any DeepLinkedStartCommandHandler
    # because it simply catches /start command
    start_handler,

    end_turn_handler,

    audio_handler,
    sticker_handler,

    # these should be the last ones, as they are based on general regexes
    make_guess_handler,
    give_clue_handler,
]
