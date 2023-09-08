from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from loader import dp
from tgbot.config import Settings

router = Router()
dp.include_router(router)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message(F.photo)
async def photo_msg(message: Message):
    await message.answer("This is image!")


@router.message()
async def echo_handler(message: Message, config: Settings) -> None:
    try:
        print(config)
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
