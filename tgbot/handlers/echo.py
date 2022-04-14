from aiogram.types import Message

from loader import dp


@dp.message_handler()
async def bot_echo(message: Message):
    await message.answer(message.text)
