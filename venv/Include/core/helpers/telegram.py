from typing import List
from aiogram import types


def create_buttons_arr(*btns_names) -> List[types.KeyboardButton]:
    return [types.KeyboardButton(btn_name) for btn_name in btns_names]


def create_markup(*btns_names, row_width=3) -> types.ReplyKeyboardMarkup:
    btns = (types.KeyboardButton(btn_name) for btn_name in btns_names)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    markup.add(*btns)

    return markup


def create_inline_markup(*btns_data: tuple, row_width=2) -> types.InlineKeyboardMarkup:
    btns = []
    for text, callback in btns_data:
        if str(callback).__contains__("http"):
            data = {
                "text": text,
                "url": callback
            }
            btns.append(data)
        else:
            data = {
                "text": text,
                "callback_data": callback
            }
            btns.append(data)

    btns = btns
    keyboard_markup = types.InlineKeyboardMarkup(row_width=row_width)
    keyboard_markup.add(*btns)
    return keyboard_markup

def create_inline_markup_hard(*buttons_data: tuple, row_width=2) -> types.InlineKeyboardMarkup:
    buttons = (types.InlineKeyboardButton(text, callback_data=callback) for text, callback in buttons_data)

    keyboard_markup = types.InlineKeyboardMarkup(row_width=row_width)
    keyboard_markup.add(*buttons)

    return keyboard_markup