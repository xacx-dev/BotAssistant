from aiogram import types
from config import dp,bot
from .messages import *
from aiogram.dispatcher import FSMContext
from Include.core.states import AddGroups
from Include.core.helpers.requestsApi import *
from Include.core.helpers import telegram as tg_helper
import openpyxl


@dp.callback_query_handler(text='create_newsletter',state="*")
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
    text=select_group,reply_markup=get_groups_btn())

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("group"),state="*")
async def manage_group(callback_query: types.CallbackQuery):
    groupid = str(callback_query.data).split("_")[1]
    chats = get_chats_in_group(groupid)
    btns = {
        ("Удалить группу", "removegroup_"+str(groupid)),
        ("Удалить чат", "remove_chat"),
        ("Назад", "create_newsletter"),
        ("Рассылка в группу", "create_newsletter_group")
    }
    group_manager = tg_helper.create_inline_markup(*btns)
    text = 'Чаты в этой группе:\n'
    i=0
    for chat in chats:
        i+=1
        text = text+str(i)+" ("+str(chat['id'])+"). "+str(chat['name'])+"\n"
    await bot.edit_message_text(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                          text=text,reply_markup=group_manager)





def get_groups_btn():
    groups = get_groups()
    data_list = []
    for group in groups:
        tulist = (str(group['name']), "group_"+ str(group['id']))
        data_list.append(tulist)
    btns = tg_helper.create_inline_markup(*data_list, row_width=2)
    return btns



















@dp.message_handler(state=AddGroups.GetFile, content_types=['document'])
async def get_names(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        print(message)
        file = await bot.get_file(message.document.file_id)
        file_path = file.file_path
        await bot.download_file(file_path, message.document.file_name)
        try:
            wb = openpyxl.load_workbook(message.document.file_name)
            sheetes = wb.get_sheet_names()
            sheet = wb.get_sheet_by_name(sheetes[0])
            rows = sheet.max_row
            groups = []
            groups.append(data['name'])
            for i in range(1, rows + 1):
                cell = sheet.cell(row=i, column=1).value
                groups.append(cell)
        except:
            await bot.send_message(message.from_user.id, text=file_error)
        add_groups(groups)
        await bot.send_message(message.from_user.id,text=good_loaded,reply_markup=START_INLINE_BTN)


@dp.message_handler(lambda message: message.text, state=AddGroups.NewGroupName, content_types=types.ContentTypes.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await AddGroups.next()
        await bot.send_message(message.from_user.id,send_me_file)

@dp.callback_query_handler(text='create_group',state="*")
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,text=new_gropu_name)
    await AddGroups.NewGroupName.set()




