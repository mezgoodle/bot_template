from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound
from loguru import logger

from tgbot.config import load_config


async def on_startup_notify(dp: Dispatcher):
    logger.info('Start admins notification')

    config = load_config()
    admins = config.tg_bot.admins

    for admin in admins:
        try:
            await dp.bot.send_message(
                admin, 'Bot has been started', disable_notification=True
            )
        except ChatNotFound:
            logger.debug(f'Chat with {admin} not found')
