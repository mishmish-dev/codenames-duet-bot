[![Build Status](https://travis-ci.com/cekc/codenames-tgbot.svg?branch=master)](https://travis-ci.com/cekc/codenames-tgbot)

# codenames-tgbot

## Running the bot

`python -m codenames.bot [options...]`

## Repository structure

### [`codenames`](https://github.com/cekc/codenames-tgbot/tree/master/codenames)

Python package containing all the logic. Needs Python version `>=3.7`.

### [`tests`](https://github.com/cekc/codenames-tgbot/tree/master/tests)

Tests for the package. To run: `python -m pytest tests`.

The tests run automatically in [Travis CI](https://travis-ci.com/cekc/codenames-tgbot). See [config](https://github.com/cekc/codenames-tgbot/blob/master/.travis.yml).

## Heroku deployment

You have to enable Postgres database for your application and set `BOT_TOKEN` and `HEROKUAPP_NAME` config variables. See [`Procfile`](https://github.com/cekc/codenames-tgbot/blob/master/Procfile).
