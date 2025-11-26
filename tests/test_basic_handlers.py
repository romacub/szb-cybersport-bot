import pytest

from src.bot.handlers.basic import cmd_ping, cmd_start


class DummyMessage:
    def __init__(self):
        self.answers: list[str] = []

    async def answer(self, text: str):
        self.answers.append(text)


@pytest.mark.anyio("asyncio")
async def test_cmd_start_response():
    message = DummyMessage()

    await cmd_start(message)

    assert message.answers == ["Привет! Я живой Telegram-бот на aiogram 🐍 (IPv4 only)"]


@pytest.mark.anyio("asyncio")
async def test_cmd_ping_response():
    message = DummyMessage()

    await cmd_ping(message)

    assert message.answers == ["pong"]
