from aiogram import types
from config import dp
from Include.core.handlers.inlinequeries.messages import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(msg_start,reply_markup=START_INLINE_BTN)


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Действие отменено', reply_markup=types.ReplyKeyboardRemove())
