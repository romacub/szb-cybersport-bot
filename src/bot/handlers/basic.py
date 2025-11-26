from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()

START_TEXT = "Привет! Я живой Telegram-бот на aiogram 🐍 (IPv4 only)"
PING_TEXT = "pong"


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(START_TEXT)


@router.message(Command("ping"))
async def cmd_ping(message: Message) -> None:
    await message.answer(PING_TEXT)
