import logging

from aiogram import Bot
from aiogram.exceptions import AiogramError

from tgbot.config import config


async def on_startup_notify(bot: Bot):
    logging.info("Start admins notification")

    admins = config.admins

    for admin in admins:
        try:
            await bot.send_message(admin, "Bot started")
        except AiogramError:
            logging.debug(f"Chat with {admin} not found")
