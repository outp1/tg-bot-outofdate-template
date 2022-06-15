from aiogram import executor

from loader import dp
from data import config
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils import botlogging 


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    # await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    # Запускаем Main логирование
    logger = botlogging.BotLogging(logger_name='AppInit', logs_dir=config.LOGS_DIR, bot_token=config.LOGS_BOT_TOKEN, 
            bot_nickname=config.BOT_NAME, admin=config.ADMINS)
    logger = logger.get_logger()
    executor.start_polling(dp, on_startup=on_startup)
