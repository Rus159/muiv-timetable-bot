import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from aiogram.types import ChatActions
from dotenv import load_dotenv
from keyboard import Keyboard
from htmltopic import get_picture
import excel


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
@dp.message_handler(filters.Text(contains='Вернуться'))
async def process_start_command(message: types.Message):
    excel.check_file_update()
    user_id = message.from_user.id
    if user_id not in excel.user_xls_association:
        excel.user_xls_file.append(excel.excelFile())
        excel.user_xls_association.update([(user_id, len(excel.user_xls_file)-1)])
    else:
        excel.user_xls_file[excel.user_xls_association[user_id]] = excel.excelFile() 
    message_ = 'Чтобы получить расписание выбери курс'
    await message.reply(message_, reply_markup=Keyboard(excel\
        .get_sheetnames(excel.user_xls_file[excel.user_xls_association[user_id]])).get_buttons())
    print(excel.user_xls_association)


@dp.message_handler(filters.Text(contains='курс'))
async def process_course_button(message: types.Message):
    user_id = message.from_user.id
    if user_id not in excel.user_xls_association:
        excel.user_xls_file.append(excel.excelFile())
        excel.user_xls_association.update([(user_id, len(excel.user_xls_file)-1)])
    else:
        excel.user_xls_file[excel.user_xls_association[user_id]] = excel.excelFile() 
    excel.user_xls_file[excel.user_xls_association[user_id]] = excel.\
        user_xls_file[excel.user_xls_association[user_id]].parse(sheet_name=message.text)
    message_ = 'Выбери группу'
    await message.reply(message_, reply_markup=Keyboard(excel.get_groupnames(excel.user_xls_file[excel.user_xls_association[user_id]])).get_buttons())


@dp.message_handler(filters.Text(contains='Д'))
async def process_group_button(message: types.Message):
    user_id = message.from_user.id
    if message.text in excel.\
       get_groupnames(excel.user_xls_file[excel.user_xls_association[user_id]]):
        await bot.send_chat_action(user_id, ChatActions.UPLOAD_PHOTO)
        await message.reply_photo(get_picture(excel.\
            get_week_timetable(message.text, excel.user_xls_file[excel.user_xls_association[user_id]])))


if __name__ == '__main__':
    executor.start_polling(dp)


''', reply_markup=ReplyKeyboardRemove()
type(excel.timetable).__name__ != 'DataFrame' and
'''
