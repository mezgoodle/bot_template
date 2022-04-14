from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart


async def admin_start(message: Message):
    await message.reply(f'Hello, {message.from_user.username}!')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, CommandStart(), state='*', is_admin=True)
