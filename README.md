[![Build Status](https://travis-ci.com/cekc/codenames-duet-bot.svg?branch=master)](https://travis-ci.com/cekc/codenames-duet-bot)

# codenames-duet-bot

## Running the bot

The bot works with Python `3.9`.

Command: `python -m codenames.bot [options...]`

## Testing the bot

Command: `python -m pytest tests`

[The tests](https://github.com/cekc/codenames-duet-bot/tree/master/tests) run automatically in [Travis CI](https://travis-ci.com/cekc/codenames-duet-bot). See [config](https://github.com/cekc/codenames-duet-bot/blob/master/.travis.yml).

## Heroku deployment

You have to enable Postgres database for your application and set `BOT_TOKEN` and `HEROKUAPP_NAME` config variables. See [`Procfile`](https://github.com/cekc/codenames-duet-bot/blob/master/Procfile).
