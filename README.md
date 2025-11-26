# szb-cybersport-bot

Telegram bot for handling SZB-Sber cybersport activities built with aiogram 3.

## Requirements

- Python 3.10+
- Virtual environment recommended (`python -m venv .venv`)

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Environment variables

Create a `.env` file (or export variables in your shell) with:

```
BOT_TOKEN=<your-telegram-bot-token>
```

## Running the bot locally

Activate your virtual environment, ensure `BOT_TOKEN` is available, then start the bot:

```bash
python -m src.main
```

The bot forces IPv4-only connections to Telegram Bot API; the session implementation lives in `src/bot/network.py`.

## Running tests

After installing dependencies, run:

```bash
pytest
```

Basic handler tests cover `/start` and `/ping` responses.
