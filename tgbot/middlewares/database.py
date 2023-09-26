from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from tgbot.misc.database import Database


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, db_instance: Database) -> None:
        self.db = db_instance

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        data["db"] = self.db
        return await handler(event, data)
