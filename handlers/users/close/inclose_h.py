from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from utils import botlogging


# Inline close button handler 
@dp.callback_query_handler(text='inclose')
async def inclose_h(call: types.CallbackQuery, state: FSMContext):
    try: 
        await state.finish()
    except: 
        pass
    await bot.delete_message(chat_id=call.message.chat.id, 
            message_id=call.message.message_id)
