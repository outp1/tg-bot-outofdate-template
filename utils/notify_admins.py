import logging

from aiogram import Dispatcher

from data import config

async def on_startup_notify(dp: Dispatcher):
    for admin in config.ADMINS:
        try:
<<<<<<< HEAD
            await dp.bot.send_message(admin, f"Бот Запущен")
=======
            await dp.bot.send_message(admin, f"{config.BOTNICK} Бот Запущен")
>>>>>>> f15fcd1... 'm'

        except Exception as err:
            logging.exception(err)
