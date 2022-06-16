import logging

from aiogram import Dispatcher

from data import config

async def on_startup_notify(dp: Dispatcher):
    for admin in config.ADMINS:
        await dp.bot.send_message(admin, f"Бот Запущен")
