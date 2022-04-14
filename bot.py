import logging

from aiogram import Dispatcher, executor

from tgbot.filters.admin import IsAdminFilter
from tgbot.middlewares.db import DbMiddleware
from tgbot.services.setting_commands import set_default_commands
from loader import dp

logger = logging.getLogger(__name__)


def register_all_middlewares(dispatcher: Dispatcher):
    logger.info('Registering middlewares')
    dispatcher.setup_middleware(DbMiddleware())


def register_all_filters(dispatcher: Dispatcher):
    logger.info('Registering filters')
    dispatcher.filters_factory.bind(IsAdminFilter)


def register_all_handlers(dispatcher: Dispatcher):
    from tgbot import handlers
    logger.info('Registering handlers')
    return


async def register_all_commands(dispatcher: Dispatcher):
    logger.info('Registering commands')
    await set_default_commands(dispatcher.bot)


async def on_startup(dispatcher: Dispatcher):
    register_all_middlewares(dispatcher)
    register_all_filters(dispatcher)
    register_all_handlers(dispatcher)
    await register_all_commands(dispatcher)
    logger.info('Bot started')


async def on_shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    logger.info('Bot shutdown')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    try:
        executor.start_polling(
            dp,
            skip_updates=True,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
        )
    except KeyboardInterrupt:
        logger.info("Stopping bot")
