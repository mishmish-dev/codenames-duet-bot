#!/usr/bin/env sh
echo "Run command is: python -m codenames.bot --token ""${BOT_TOKEN}"" --db ""${DATABASE_URL}"" --webhook-url ""https://${HOST}/${BOT_TOKEN}"" --listen-address 0.0.0.0 --listen-port ""${PORT}"" ""${DEBUG_MODE}"
python -m codenames.bot --token "${BOT_TOKEN}" --db "${DATABASE_URL}" --webhook-url "https://${HOST}/${BOT_TOKEN}" --listen-address 0.0.0.0 --listen-port "${PORT}" "${DEBUG_MODE}"
