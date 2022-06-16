from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import IN_CLOSE_TEXT

def inclose(text: str = IN_CLOSE_TEXT, callback: str = 'inclose'):
    b = InlineKeyboardMarkup()
    print('\n', text, callback)
    b.add(InlineKeyboardButton(text=text, callback_data=callback))
    return b
