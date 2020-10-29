from aiogram import types
from core.helpers import telegram as tg_helper

new_gropu_name='Введите название для нвоой группы\n/cancel - для отмены операции'
send_me_file='Пришлите Excel файл с названиями чатов (групп)\n/cancel - для отмены операции'
good_loaded='Группы успешно загружены\nВыберите действие'

file_error='Ошибка! Проверьте формат файла и его состояние!'

select_group='Выберите группу'




btns = {
    ("Создать группу", "create_group"),
    ("Сделать рассылку", "create_newsletter")
}
START_INLINE_BTN = tg_helper.create_inline_markup(*btns)


# -- Start Messages
msg_start = 'Выберите функцию'

