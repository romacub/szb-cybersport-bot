import pytest
from unittest.mock import AsyncMock

from src.bot.handlers.basic import PING_TEXT, START_TEXT, cmd_ping, cmd_start


@pytest.mark.asyncio
async def test_cmd_start_sends_greeting():
    message = AsyncMock()

    await cmd_start(message)

    message.answer.assert_awaited_once_with(START_TEXT)


@pytest.mark.asyncio
async def test_cmd_ping_sends_pong():
    message = AsyncMock()

    await cmd_ping(message)

    message.answer.assert_awaited_once_with(PING_TEXT)
