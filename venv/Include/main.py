from aiogram import executor
from loguru import logger
from config import *
import core.handlers
import core.helpers
import asyncio

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


