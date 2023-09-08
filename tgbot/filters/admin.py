from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Settings


class IsAdminFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    async def __call__(self, message: Message, config: Settings) -> bool:
        return message.from_user.id in config.admins
