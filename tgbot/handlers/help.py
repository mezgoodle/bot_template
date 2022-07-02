from aiogram.types import Message
from aiogram.dispatcher.filters import CommandHelp

from loader import dp
from tgbot.keyboards.inline.help_keyboard import create_markup


@dp.message_handler(CommandHelp(), state='*')
async def help_command(message: Message) -> Message:
    markup = create_markup()
    await message.reply(f'Hello, {message.from_user.username}!', reply_markup=markup)
