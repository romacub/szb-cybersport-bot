from aiogram import Dispatcher

from . import basic

__all__ = ["setup_handlers"]


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(basic.router)
