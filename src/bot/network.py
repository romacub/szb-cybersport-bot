import socket

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession


class IPv4AiohttpSession(AiohttpSession):
    """Custom AiohttpSession that forces IPv4 connections."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Важно: говорим TCPConnector использовать только IPv4
        self._connector_init["family"] = socket.AF_INET


def create_bot(token: str) -> Bot:
    session = IPv4AiohttpSession()
    return Bot(token, session=session)
