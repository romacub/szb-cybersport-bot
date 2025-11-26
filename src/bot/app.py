import logging

from aiogram import Dispatcher

from .config import get_settings, setup_logging
from .handlers import setup_handlers
from .network import create_bot

POLLING_LOG_MESSAGE = "Starting bot polling (IPv4 forced)..."


async def run_app() -> None:
    setup_logging()
    settings = get_settings()

    bot = create_bot(settings)

    dp = Dispatcher()
    setup_handlers(dp)

    logging.info(POLLING_LOG_MESSAGE)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
