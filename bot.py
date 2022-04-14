import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.filters.admin import IsAdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.user import register_user
from tgbot.middlewares.db import DbMiddleware

logger = logging.getLogger(__name__)
config = load_config()
storage = MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
bot['config'] = config


def register_all_middlewares(dispatcher: Dispatcher):
    logger.info('Registering middlewares')
    dispatcher.setup_middleware(DbMiddleware())


def register_all_filters(dispatcher: Dispatcher):
    logger.info('Registering filters')
    dispatcher.filters_factory.bind(IsAdminFilter)


def register_all_handlers(dispatcher: Dispatcher):
    logger.info('Registering handlers')
    register_admin(dispatcher)
    register_user(dispatcher)
    register_echo(dispatcher)


async def on_startup(dispatcher: Dispatcher):
    register_all_middlewares(dispatcher)
    register_all_filters(dispatcher)
    register_all_handlers(dispatcher)
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
