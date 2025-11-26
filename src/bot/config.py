import logging
import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv


LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def setup_logging() -> None:
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


@dataclass(frozen=True)
class Settings:
    bot_token: str


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise RuntimeError("BOT_TOKEN is not set in environment or .env file")

    return Settings(bot_token=bot_token)
