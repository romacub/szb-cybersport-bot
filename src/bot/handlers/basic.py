from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("Привет! Я живой Telegram-бот на aiogram 🐍 (IPv4 only)")


@router.message(Command("ping"))
async def cmd_ping(message: Message) -> None:
    await message.answer("pong")
