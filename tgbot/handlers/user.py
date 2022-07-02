from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from loader import dp
from tgbot.keyboards.reply.state_keyboard import create_markup
from tgbot.states.states import Example
from tgbot.middlewares.throttling import rate_limit


@dp.message_handler(CommandStart(), state="*")
@rate_limit(5, 'start')
async def user_command(message: Message) -> Message:
    await Example.first()
    markup = create_markup()
    await message.reply("Hello, user!", reply_markup=markup)
