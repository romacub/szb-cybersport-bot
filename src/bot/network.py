import socket

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession

from .config import Settings


class IPv4AiohttpSession(AiohttpSession):
    """Custom AiohttpSession that forces IPv4 connections."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Важно: говорим TCPConnector использовать только IPv4
        self._connector_init["family"] = socket.AF_INET


def create_bot(settings: Settings) -> Bot:
    session = IPv4AiohttpSession()
    return Bot(settings.bot_token, session=session)
