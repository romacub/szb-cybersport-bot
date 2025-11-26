import asyncio
import logging
import os
import socket

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

from aiogram.client.session.aiohttp import AiohttpSession


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in .env")


# Кастомная сессия, форсим IPv4
class IPv4AiohttpSession(AiohttpSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ВАЖНО: говорим TCPConnector использовать только IPv4
        self._connector_init["family"] = socket.AF_INET


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("Привет! Я живой Telegram-бот на aiogram 🐍 (IPv4 only)")


@router.message(Command("ping"))
async def cmd_ping(message: Message) -> None:
    await message.answer("pong")


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    session = IPv4AiohttpSession()
    bot = Bot(BOT_TOKEN, session=session)

    dp = Dispatcher()
    dp.include_router(router)

    logging.info("Starting bot polling (IPv4 forced)...")
    try:
        await dp.start_polling(bot)
    finally:
        # аккуратно закрываем сессию, чтобы не было warning'ов
        s = await bot.get_session()
        await s.close()


if __name__ == "__main__":
    asyncio.run(main())
