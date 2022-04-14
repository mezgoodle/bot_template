from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), state='*', is_admin=True)
async def admin_start(message: Message):
    await message.reply(f'Hello, {message.from_user.username}!')
