import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
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
    dispatcher.filters_factory.bind(AdminFilter)


def register_all_handlers(dispatcher: Dispatcher):
    logger.info('Registering handlers')
    register_admin(dispatcher)
    register_user(dispatcher)
    register_echo(dispatcher)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
        logger.info("Starting bot")
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        logger.info("Bot stopped")
