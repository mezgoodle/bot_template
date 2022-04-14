from aiogram import Dispatcher
from aiogram.types import Message


async def bot_echo(message: Message):
    await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
