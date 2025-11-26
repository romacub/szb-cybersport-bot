import logging
import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv


@dataclass
class Settings:
    bot_token: str


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def load_environment() -> None:
    load_dotenv()


def _build_settings() -> Settings:
    load_environment()
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise RuntimeError("BOT_TOKEN is not set in .env")
    return Settings(bot_token=bot_token)


def get_settings() -> Settings:
    return _cached_settings()


@lru_cache(maxsize=1)
def _cached_settings() -> Settings:
    return _build_settings()
