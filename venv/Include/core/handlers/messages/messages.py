from aiogram import types
from core.helpers import telegram as tg_helper

chats_msg = 'Ты бы хотел узнавать актуальную информацию о мероприятиях Фонда?'
chats = {
    ("Хочу всё знать!", "chat_1"),
    ("Я уже знаю.", "chat_2")
}

chats2 = tg_helper.create_inline_markup(*chats)

finder_msg = 'В данном меню, ты можешь осуществить поиск пользователя.\nВыберите параметр по которому будет осуществлен' \
             'поиск'
finders_type = {
    ("По фамилии", "finder_lastname"),
    ("По сыллке вк.", "finder_vk"),
    ("По сыллке файсбук.", "finder_fb"),
    ("По telegram_id", "finder_tg"),
    ("По ", "finder_tg"),
    ("По telegram_id", "finder_tg")
}

finder_btn = tg_helper.create_inline_markup(*finders_type)


user_profile_text = 'В данном меню, вы можете работать со свои профилем'
user_profile = {

    ("О проекте", "userprofile_project"),
    ("О учебе", "userprofile_study"),

    ("О работе", "userprofile_work"),
    ("О интересах", "userprofile_hobby"),

    ("О компетенции", "userprofile_competence"),
    ("Изменить информацию", "userprofile_edit")
}

user_profile_btn = tg_helper.create_inline_markup(*user_profile)

