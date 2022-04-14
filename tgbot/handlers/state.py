import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp
from tgbot.states.states import Example


@dp.message_handler(state=Example.example)
async def user_start(message: Message, state: FSMContext):
    logger = logging.getLogger(__name__)
    logger.info('Handler executed')

    await state.finish()
    await message.reply(f'Your state: {message.text}')
