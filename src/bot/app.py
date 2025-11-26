import logging

from aiogram import Dispatcher

from .config import BOT_TOKEN, setup_logging
from .handlers import basic
from .network import create_bot


POLLING_LOG_MESSAGE = "Starting bot polling (IPv4 forced)..."


async def run_app() -> None:
    setup_logging()

    bot = create_bot(BOT_TOKEN)

    dp = Dispatcher()
    dp.include_router(basic.router)

    logging.info(POLLING_LOG_MESSAGE)
    try:
        await dp.start_polling(bot)
    finally:
        session = await bot.get_session()
        await session.close()
