from aiogram import Dispatcher

from .basic import router as basic_router

__all__ = ["register_handlers"]


def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(basic_router)
