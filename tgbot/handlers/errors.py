from typing import Optional

from aiogram.utils.exceptions import (TelegramAPIError,
                                      MessageNotModified,
                                      CantParseEntities)
from loguru import logger

from loader import dp



@dp.errors_handler()
async def errors_handler(update, exception) -> Optional[bool]:
    if isinstance(exception, MessageNotModified):
        logger.error('Message is not modified')
        # do something here?
        return True

    if isinstance(exception, CantParseEntities):
        # or here
        logger.error(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    #  MUST BE THE  LAST CONDITION
    if isinstance(exception, TelegramAPIError):
        logger.error(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    # At least you have tried.
    logger.error(f'Update: {update} \n{exception}')
