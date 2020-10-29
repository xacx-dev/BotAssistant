from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class AddGroups(StatesGroup):
    NewGroupName = State()
    GetFile = State()


class MessageToGroup(StatesGroup):
    WriteAndSendMSG = State()

