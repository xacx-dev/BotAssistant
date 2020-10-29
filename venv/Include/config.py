import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_token = '1100745663:AAHkv5lBcbOAe2J-nRi0SAx4OT_XxiPmCao'
req_url = 'http://194.67.111.246:82/api/v1'



storage = MemoryStorage()
bot = Bot(token=bot_token,parse_mode='html')
dp = Dispatcher(bot, storage=storage)
#logging.basicConfig(level=logging.INFO)


