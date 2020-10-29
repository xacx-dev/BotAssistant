from aiogram import types
from core.helpers import telegram as tg_helper

new_gropu_name='Введите название для нвоой группы\n/cancel - для отмены операции'
send_me_file='Пришлите Excel файл с названиями чатов (групп)\n/cancel - для отмены операции'
good_loaded='Группы успешно загружены\nВыберите действие'

file_error='Ошибка! Проверьте формат файла и его состояние!'

select_group='Выберите группу'
group_deleted='Группа удалена'

msg_sended='Сообщение отправлено!'
write_msg='Введите сообщение!\n/cancel - для отмены операции'

chat_del_msg='Введите id чата для удаления(в скобочках)\n/cancel - для отмены операции'
chat_del_err='Ошибка! неверный id чата'
chat_deleted='Чат удален!'

btns = {
    ("Создать группу", "create_group"),
    ("Сделать рассылку", "create_newsletter")
}
START_INLINE_BTN = tg_helper.create_inline_markup(*btns)


# -- Start Messages
msg_start = 'Выберите функцию'

