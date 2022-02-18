from aiogram import executor

from loader import dp
<<<<<<< HEAD
from data import config
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils import botlogging 
=======
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
>>>>>>> f15fcd1... 'm'


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
<<<<<<< HEAD
    # await set_default_commands(dispatcher)
=======
    await set_default_commands(dispatcher)
>>>>>>> f15fcd1... 'm'

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

<<<<<<< HEAD
if __name__ == '__main__':
    # Запускаем Main логирование
    logger = botlogging.BotLogging(logger_name='AppInit', logs_dir=config.LOGS_DIR, bot_token=config.LOGS_BOT_TOKEN, 
            bot_nickname=config.BOT_NAME, admin=config.ADMINS)
    logger = logger.get_logger()
    executor.start_polling(dp, on_startup=on_startup)
=======

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

>>>>>>> f15fcd1... 'm'
