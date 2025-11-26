# szb-cybersport-bot

Telegram-бот для работы с киберспортивным сообществом на базе **aiogram 3**.

## Подготовка окружения

1. Создайте и активируйте виртуальное окружение, например:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Создайте файл `.env` в корне проекта и укажите токен бота:
   ```bash
   BOT_TOKEN=your_telegram_bot_token
   ```

## Запуск бота

После активации окружения и заполнения `.env` запустите бота командой:
```bash
python -m src.main
```

## Запуск тестов

Для проверки базовых хендлеров выполните:
```bash
pytest
```
