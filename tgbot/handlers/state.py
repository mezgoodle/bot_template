from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp
from tgbot.states.states import Example


@dp.message_handler(state=Example.example)
async def state_handler(message: Message, state: FSMContext) -> Message:
    await state.finish()
    await message.reply(f"Your state: {message.text}")
