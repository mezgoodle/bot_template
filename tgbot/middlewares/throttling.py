from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from cachetools import TTLCache

THROTTLE_TIME_OTHER = 1


class ThrottlingMiddleware(BaseMiddleware):
    caches = {
        "default": TTLCache(maxsize=10_000, ttl=THROTTLE_TIME_OTHER),
    }

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        throttling_key = get_flag(
            handler=data, name="throttling_key", default="default"
        )
        if throttling_key is not None and throttling_key in self.caches:
            if event.chat.id in self.caches[throttling_key]:
                return
            else:
                self.caches[throttling_key][event.chat.id] = None
        return await handler(event, data)
