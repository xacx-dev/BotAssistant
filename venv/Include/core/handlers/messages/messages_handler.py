from aiogram import types
from config import dp,bot,req_url
from Include.core.helpers import requestsApi
from .messages import *




@dp.message_handler()
async def process_chat_command(message: types.Message):
    message.text = str(message.text).lower()
    print(message.text)

