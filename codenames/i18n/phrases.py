from codenames.i18n.language import _Language

RUSSIAN = _Language.RUSSIAN
ENGLISH = _Language.ENGLISH
PERSIAN = _Language.PERSIAN


# common

AND = {
    RUSSIAN: "и",
    ENGLISH: "and",
    PERSIAN: "و" 
}

NOBODY = {
    RUSSIAN: "никто",
    ENGLISH: "nobody",
    PERSIAN: "هیچکس" 
}

SUCCESS = {
    RUSSIAN: "Успешно!",
    ENGLISH: "Success!",
    PERSIAN: "باموفقیت انجام شد!" 
}

CANCELLED = {
    RUSSIAN: "Ввод отменён.",
    ENGLISH: "Cancelled input.",
    PERSIAN: "ورودی لغو شد"
}

DONT_UNDERSTAND = {
    RUSSIAN: "Я вас не понимаю.",
    ENGLISH: "I don't understand you.",
    PERSIAN: "متوجه نشدم."
}


# help

HELP_MESSAGE = {
    RUSSIAN: (
        "Приветствую! Я — бот, с помощью которого вы "
        "можете играть в Codenames.Duet со своими друзьями."
    ),

    ENGLISH: (
        "Hello! I am bot that will allow you to play "
        "Codenames.Duet with your friends."
    ),
    PERSIAN: (
        " سلام! شما به وسیله این ربات می‌تونید بازی کدنیمز رو با دوستانتون بازی کنید."
    )
}

CREATE_GAME_INLINE = {
    RUSSIAN: "создать игру",
    ENGLISH: "create a game",
    PERSIAN: "ساخت بازی"
}

TOKEN_COUNT_SETTING = {
    RUSSIAN: "{} ходов",
    ENGLISH: "{} turns",
    PERSIAN: "{} فرصت" 
}

CREATE_GAME_WITH_SETTINGS = {
    RUSSIAN: "✅ :: {token_count} ходов, {wordlist} :: ✅",
    ENGLISH: "✅ :: {token_count} turns, {wordlist} :: ✅",
    PERSIAN: "✅ :: {token_count} فرصت, {wordlist} :: ✅"
}

GAME_CREATED = {
    RUSSIAN: "Игра создана.",
    ENGLISH: "Game created.",
    PERSIAN: "بازی ساخته شد."
}


# join

JOIN_GAME_AUTO_TEAM = {
    RUSSIAN: "присоединиться (автовыбор стороны)",
    ENGLISH: "join (choose side automatically)",
    PERSIAN: "ورود به بازی (انتخاب تیم به صورت اتفاقی)"
}

JOIN_GAME_FIRST_TEAM = {
    RUSSIAN: "к первой",
    ENGLISH: "join the first",
    PERSIAN: "ورود به تیم اول"
}

JOIN_GAME_SECOND_TEAM = {
    RUSSIAN: "ко второй",
    ENGLISH: "join the second",
    PERSIAN: "ورود به تیم دوم"
}

CHOOSE_NEW_GAME_SETTINGS = {
    RUSSIAN: "Задайте параметры игры:",
    ENGLISH: "Set parameters for the game:",
    PERSIAN: "تعیین پارامتر برای بازی:"
}

ALREADY_IN_GAME = {
    RUSSIAN: (
        "Вы уже играете. Если вы действительно хотите начать новую игру, "
        "покиньте текущую командой /leave_game."
    ),
    ENGLISH: (
        "You are already in a game. If you really want to start a new one, "
        "leave the current with /leave_game command."
    ),
    PERSIAN: (
        " شما در حال حاضر در یک بازی حضور دارید. اگر می‌خواهید می‌توانید با ارسال دستور /leave_game بازی را ترک کنید. "
    )
}

LEFT_GAME = {
    RUSSIAN: "Вы покинули игру.",
    ENGLISH: "You left the game.",
    PERSIAN: "شما بازی رو ترک کردید."
}

YOU_ARE_NOT_IN_GAME = {
    RUSSIAN: "Вы не в игре.",
    ENGLISH: "You are not in game.",
    PERSIAN: "شما در بازی حضور ندارید." 
}

INVITATION = {
    RUSSIAN: (
        "Ваши друзья могут присоединиться, нажав на кнопку ниже. "
        "Вы можете переслать им это сообщение или отправить ссылку кнопки.\n\n"
        "На текущий момент за первым торцом стола {first_team}, а "
        "за вторым — {second_team}."
    ),
    ENGLISH: (
        "Your friends can join by tapping the button below. "
        "You can forward this message to them or just share button's link.\n\n"
        "Currently, the first table side is taken by {first_team}, while "
        "the second side is {second_team}."
    ),
    PERSIAN: (
        "شما با زدن بر روی دکمه زیر می‌توانید دوستان خود را به بازی بیاورید. "
        " شما می‌توانید این پیام را فوروارد کنید یا اینکه لینک دکمه را به اشتراک بگذارید.\n\n"
        "Currently, the first table side is taken by {first_team}, while "
        "the second side is {second_team}."
    )
}


## replay

REPLAY = {
    RUSSIAN: "{} начинает игру заново.",
    ENGLISH: "{} starts the game over.",
    PERSIAN: "{} بازی را دوباره شروع کرد."
}


## ping

USERNAME_REMINDS = {
    RUSSIAN: "{} напоминает:",
    ENGLISH: "{} reminds:",
    PERSIAN: "{} یادآوری می‌کند:"
}

REMINDER_SENT = {
    RUSSIAN: "Напоминание отправлено.",
    ENGLISH: "Reminder sent.",
    PERSIAN: "یاداوری ارسال شد."
}

ANYONE_CAN_GIVE_CLUE = {
    RUSSIAN: "Сейчас любой игрок может дать дать подсказку.",
    ENGLISH: "Any player can give clue now.",
    PERSIAN: "الان همه‌ی بازیکنان می‌توانند سرنخ بدهند" 
}

YOU_NOW_GIVE_CLUE = {
    RUSSIAN: "Вы сейчас даёте подсказку.",
    ENGLISH: "You now give clue.",
    PERSIAN: "شما می‌توانید سرنخ بدهید." 
}

YOU_NOW_MAKE_GUESS_CANNOT_SKIP = {
    RUSSIAN: "Вы сейчас отгадываете агента (закончить ход нельзя).",
    ENGLISH: "You now make guess (you can't end turn now).",
    PERSIAN: "شما  می‌توانید حدس بزنید (نمی‌توانید نوبت را به اتمام برسانید)."
}

YOU_NOW_MAKE_GUESS = {
    RUSSIAN: "Вы сейчас отгадываете агента.",
    ENGLISH: "You now make guess.",
    PERSIAN: "حالا شما حدس بزنید." 
}

ALL_MAKE_GUESS_SUDDEN_DEATH = {
    RUSSIAN: "Запас ходов исчерпан. Сейчас все игроки вне очереди открывают оставшихся агентов.",
    ENGLISH: "Ran out of time. Now all players are guessing their remained agents.",
    PERSIAN: "وقت تمام شد. حالا تمام بازیکنان مأموران باقی مانده را حدس بزنند."
}

GAME_IS_OVER_REPLAY = {
    RUSSIAN: "Партия окончена. Как насчёт /replay ?",
    ENGLISH: "Game is over. /replay ?",
    PERSIAN: "بازی تمام شد. اگر میخواهید دوباره بازی کنید /replay را بفرستید."
}


# play

## give clue

CLUE_ACCEPTED = {
    RUSSIAN: "Подсказка принята.",
    ENGLISH: "Clue accepted.",
    PERSIAN: "سرنخ تأیید شد."
}

PLAYER_GIVES_CLUE = {
    RUSSIAN: "{nickname} даёт подсказку:\n{clue}.",
    ENGLISH: "{nickname} gives a clue:\n{clue}.",
    PERSIAN: "{nickname} یک سرنخ داد :\n{clue}."
}

NOT_YOUR_TURN_TO_GIVE_CLUE = {
    RUSSIAN: "Сейчас не очередь вашей команды давать подсказку.",
    ENGLISH: "It's not your side's turn to give clue now.",
    PERSIAN: "الان نوبت تیم شما برای سرنخ دادن نیست." 
}

NOT_GIVING_CLUE_WAIT_FOR_OTHER_TEAM = {
    RUSSIAN: "С другой стороны пока никого нет. Подсказка не дана.",
    ENGLISH: "There is no one on the other side yet. Clue not given.",
    PERSIAN: "هنوز کسی در تیم مقابل وجود ندارد. سرنخ تایید نشد."
}

CLUE_TOO_LONG = {
    RUSSIAN: "Слишком длинная подсказка. Пожалуйста, пришлите подсказку длиной не более {} символов.",
    ENGLISH: "The clue is too long. Please provide a clue that doesn't exceed {} characters.",
    PERSIAN: "سرنخ خیلی طولانی است. لطفا سرنخی ارسال کنید که از حد مجاز فراتر نرود."
}

## make guess

GUESS_ACCEPTED = {
    RUSSIAN: "Догадка принята.",
    ENGLISH: "Guess accepted.",
    PERSIAN: "حدس شما تأیید شد."
}

PLAYER_MAKES_GUESS = {
    RUSSIAN: "{nickname} называет догадку:\n{guess}.\n{result}",
    ENGLISH: "{nickname} makes a guess:\n{guess}.\n{result}",
    PERSIAN: "{nickname} یک حدس زد:\n{guess}.\n{result}"
}

BUMPED_INTO_AGENT = {
    RUSSIAN: "В яблочко! Это агент!",
    ENGLISH: "Bull's eye! It's an agent!",
    PERSIAN: "زدی تو خال! این یک مأمور مخفی بود!" 
}

BUMPED_INTO_BYSTANDER = {
    RUSSIAN: "Мимо! Это мирный житель.",
    ENGLISH: "Miss! It's a bystander.",
    PERSIAN: "حیف شد! این یک رهگذر بود." 
}

BUMPED_INTO_ASSASSIN = {
    RUSSIAN: "Пиф-паф! Это убийца.",
    ENGLISH: "Bang bang! It's an assassin.",
    PERSIAN: "بنگ بنگ! این یک قاتل بود." 
}

SUDDEN_DEATH = {
    RUSSIAN: "Упс! Вы исчерпали все свои ходы. Игроки вне очереди пытаются дооткрыть своих агентов.",
    ENGLISH: "Oops! You have no turns left. Now players try out of turn to reveal their agents.",
    PERSIAN: " ای وای! فرصت های شما به اتمام رسید. حالا بازیکنان می‌توانند آخرین تلاش خود را برای پیدا کردن مأموران مخفی بکنند."
}

ALL_AGENTS_FROM_ONE_TEAM_FOUND = {
    RUSSIAN: "Ура! Все агенты с этой стороны открыты. Ваш ход завершён.",
    ENGLISH: "Hooray! All agents found for this side. End of your turn.",
    PERSIAN: "هورا! همه ی مأموران مخفی این تیم پیدا شدند. نوبت شما به اتمام رسید."
}

NOT_YOUR_TURN_TO_MAKE_GUESS = {
    RUSSIAN: "Сейчас не очередь вашей команды отгадывать агента.",
    ENGLISH: "It's not your side's turn to make guess now.",
    PERSIAN: "الان نوبت تیم شما برای حدی زدن نیست." 
}

UNKNOWN_CODENAME = {
    RUSSIAN: "Кодовое имя не распознано. Попробуйте дать догадку снова.",
    ENGLISH: "Couldn't identify codename. Try make guess again.",
    PERSIAN: "حرف رمز شما تشخیص داده نشد. دوباره حدس بزنید."
}


## end turn

TURN_ENDED = {
    RUSSIAN: "Вы закончили ход.",
    ENGLISH: "You ended your turn.",
    PERSIAN: "شما نوبت خود را به اتمام رساندید." 
}

PLAYER_ENDED_TURN = {
    RUSSIAN: "{} завершает ход.",
    ENGLISH: "{} ended their turn.",
    PERSIAN: "{} نوبت خود را به اتمام رساندند." 
}


## clue history

CLUE_HISTORY = {
    RUSSIAN: "История подсказок на данный момент:\n\n{}",
    ENGLISH: "Clue history so far:\n\n{}",
    PERSIAN: "تاریخچه سرنخ‌ها تا به اینجا کار:\n\n{}"
}

CLUE_HISTORY_ITEM = {
    RUSSIAN: "{team} :: {clue}",
    ENGLISH: "{team} :: {clue}",
    PERSIAN: "{team} :: {clue}"
}

CLUE_HISTORY_EMPTY = {
    RUSSIAN: "История подсказок пуста.",
    ENGLISH: "Clue history is empty.",
    PERSIAN: "تاریخچه سرنخ‌ها خالی است." 
}


# settings

CURRENT_SETTINGS = {
    RUSSIAN: (
        "Текущие настройки:\n"
        "- игровое имя: {nickname} ..:: /nickname, чтобы изменить\n"
        "- язык: {language} ..:: /language, чтобы изменить"
    ),
    ENGLISH: (
        "Current settings:\n"
        "- in-game nickname: {nickname} ..:: /nickname to change\n"
        "- language: {language} ..:: /language to change"
    ),
    PERSIAN: (
        "تنظیمات کنونی:\n"
        "- نام مستعار در بازی: {nickname} ..:: /nickname, برای تغییر\n" 
        "-زبان: {language} ..:: /language ، برای تغییر"
}

NICKNAME_DEFAULT_SETTING = {
    RUSSIAN: "{} [по умолчанию: ваше имя в Телеграме]",
    ENGLISH: "{} [default: your first name in Telegram]",
    PERSIAN: "{} [پیش فرض: نام شما در تلگرام]" 
}

LANGUAGE_DEFAULT_SETTING = {
    RUSSIAN: "{} [по умолчанию]",
    ENGLISH: "{} [default]",
    PERSIAN: "{} [پیش فرض]"
}

## language

CHOOSE_LANGUAGE = {
    RUSSIAN: "Выберите язык.",
    ENGLISH: "Choose a language.",
    PERSIAN: "زبان خود را انتخاب کنید."
}

LANGUAGE_NAME = {
    RUSSIAN: "🇷🇺 русский",
    ENGLISH: "🇬🇧 English",
    PERSIAN: "🇮🇷 فارسی" 
}

LANGUAGE_CHANGED = {
    RUSSIAN: "Язык изменён на русский.",
    ENGLISH: "Language changed to English.",
    PERSIAN: "زبان به فارسی تغییر کرد."
}

RETURN_TO_LANGUAGE_CHOICE = {
    RUSSIAN: "Отправьте /language, чтобы вернуться к выбору языка.",
    ENGLISH: "Send /language to choose again.",
    PERSIAN: "دستور /language را برای انتخاب مجدد ارسال کنید."
}


## nickname

CHANGE_NICKNAME_FROM_SET = {
    RUSSIAN: (
        "Ваше игровое имя — {}.\n"
        "Пришлите мне новое, если хотите его изменить, или /cancel, если нет.\n"
        "Отправьте /clear, чтобы очистить эту настройку."
    ),
    ENGLISH: (
        "Your in-game nickname is {}.\n"
        "Send me a new one if you want to change it or /cancel if you don't.\n"
        "You may also /clear this setting."
    ),
    PERSIAN: (
        "نام مستعار شما در بازی {}.\n"
        "اگر می‌خواهید نام مستعار خود را تغییر دهید همین الان یک نام جدید بفرستید در غیر این‌صورت /cancel را ارسال کنید.\n"
        "اگر می‌خواهید میتوانید این تنظیمات را با دستور /clear پاک کنید."
}

CHANGE_NICKNAME_FROM_NOT_SET = {
    RUSSIAN: "Введите своё игровое имя или /cancel, чтобы оставить его вашим именем в Телеграме.",
    ENGLISH: "Enter your in-game nickname or /cancel to leave it your first name in Telegram.",
    PERSIAN: "نام مستعار دلخواه خود را ارسال کنید در غیر این‌صورت با ارسال دستور /cancel نام تلگرام خود را به عنوان نام مستعار در نظر بگیرید."
}

NICKNAME_TOO_LONG = {
    RUSSIAN: "Слишком длинный ник. Пожалуйста, пришлите имя длиной не более {} символов.",
    ENGLISH: "The nickname is too long. Please provide a name that doesn't exceed {} characters.",
    PERSIAN: "نام مستعار شما خیلی بلند است. لطف نام کوتاه تری ارسال کنید."
}

NICKNAME_CLEARED = {
    RUSSIAN: "Настройка сброшена. Ваше игровое имя теперь снова ваше имя в Телеграме.",
    ENGLISH: "The setting is cleared. Your nickname is your first name in Telegram now.",
    PERSIAN: "تنظیمات پاک شدند. نام مستعار شما همان اسم شما در تلگرام خواهد بود."
}
