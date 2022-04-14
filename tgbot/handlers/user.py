from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from loader import dp

import logging


@dp.message_handler(CommandStart(), state="*")
async def user_start(message: Message):
    logger = logging.getLogger(__name__)
    logger.info('Handler executed')
    await message.reply("Hello, user!")
