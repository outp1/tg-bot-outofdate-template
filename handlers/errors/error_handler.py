import logging
from aiogram.utils.exceptions import (TelegramAPIError,
                                      MessageNotModified,
                                      CantParseEntities)

from utils import botlogging
from loader import dp

logger = botlogging.BotLogging(logger_name='Main', logs_dir=config.LOGS_DIR, bot_token=config.LOGS_BOT_TOKEN, 
            bot_nickname=config.BOT_NAME, admin=config.ADMINS)
logger = logger.get_logger()

@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    logger.error(exception)

"""
=======

>>>>>>> f15fcd1... 'm'
    if isinstance(exception, MessageNotModified):
        logging.exception('Message is not modified')
        # do something here?
        return True
      
    if isinstance(exception, CantParseEntities):
        # or here
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True
      
    #  MUST BE THE  LAST CONDITION (ЭТО УСЛОВИЕ ВСЕГДА ДОЛЖНО БЫТЬ В КОНЦЕ)
    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True
    
    # At least you have tried.
    logging.exception(f'Update: {update} \n{exception}')
<<<<<<< HEAD
    """
