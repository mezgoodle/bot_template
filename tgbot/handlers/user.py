from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def user_start(message: Message):
    await message.reply("Hello, user!")
