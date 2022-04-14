from aiogram.types import Message

from loader import dp

import logging


@dp.message_handler()
async def bot_echo(message: Message):
    logger = logging.getLogger(__name__)
    logger.info('Handler executed')
    await message.answer(message.text)
