import logging
import os

from aiogram import Dispatcher
from aiogram.utils.executor import start_polling, start_webhook
from loguru import logger

from tgbot.config import config
from tgbot.filters.admin import IsAdminFilter
from tgbot.middlewares.throttling import ThrottlingMiddleware
from tgbot.services.setting_commands import set_default_commands
from tgbot.services.admins_notify import on_startup_notify
from loader import dp


def register_all_middlewares(dispatcher: Dispatcher) -> None:
    logger.info("Registering middlewares")
    dispatcher.setup_middleware(ThrottlingMiddleware())


def register_all_filters(dispatcher: Dispatcher) -> None:
    logger.info("Registering filters")
    dispatcher.filters_factory.bind(IsAdminFilter)


def register_all_handlers(dispatcher: Dispatcher) -> None:
    from tgbot import handlers

    logger.info("Registering handlers")


async def register_all_commands(dispatcher: Dispatcher) -> None:
    logger.info("Registering commands")
    await set_default_commands(dispatcher.bot)


async def on_startup(dispatcher: Dispatcher, webhook_url: str = None) -> None:
    register_all_middlewares(dispatcher)
    register_all_filters(dispatcher)
    register_all_handlers(dispatcher)
    await register_all_commands(dispatcher)
    # Get current webhook status
    webhook = await dispatcher.bot.get_webhook_info()

    if webhook_url:
        await dispatcher.bot.set_webhook(webhook_url)
        logger.info("Webhook was set")
    elif webhook.url:
        await dispatcher.bot.delete_webhook()
        logger.info("Webhook was deleted")

    await on_startup_notify(dispatcher)

    logger.info("Bot started")


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    logger.info("Bot shutdown")


if __name__ == "__main__":
    logger.add(
        "tgbot.log",
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        rotation="10 KB",
        compression="zip",
    )
    logger.info("Initializing bot")

    # Webhook settings
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
    WEBHOOK_HOST = f"https://{HEROKU_APP_NAME}.herokuapp.com"
    WEBHOOK_PATH = f"/webhook/{config.bot_token.get_secret_value()}"
    WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
    # Webserver settings
    WEBAPP_HOST = "0.0.0.0"
    WEBAPP_PORT = int(os.getenv("PORT", 5000))

    start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )

    # start_webhook(
    #     dispatcher=dp,
    #     on_startup=functools.partial(on_startup, webhook_url=WEBHOOK_URL),
    #     on_shutdown=on_shutdown,
    #     webhook_path=WEBHOOK_PATH,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT
    # )
