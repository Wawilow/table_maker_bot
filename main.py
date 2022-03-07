"""
Install aiogram: pip3 install aiogram
https://docs.aiogram.dev/en/latest/install.html#using-pip
"""

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
                    )
logger = logging.getLogger(__name__)


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.inline_keyboard import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.dispatcher import filters
from aiogram import types

import os

from config import *
from ph import *
from data import *


bot = Bot(token=telegram_bot_token)

# storage = MemoryStorage()
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text='Hi please send me you google docs url')


@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer(text=''
                              'Send me your google docs url, '
                              'he looks like: \n«https://docs.google.com/spreadsheets/d/ YOUR FILE ID»')


@dp.message_handler(filters.Text(contains="docs.google.com"))
async def url(message: types.Message):
    """https://docs.google.com/spreadsheets/d/1TR3aZ3w4f-lf1O5csbaEA07Yn1Th_tcS-e3xMYgcXQA/edit#gid=0"""
    url = message.text
    file_id = url.split('/')
    file_id = [file_id[i + 1] for i in range(len(file_id)) if file_id[i] == "d"][0]

    user_directiry = f"""{os.path.abspath("__file__")[:-9]}\{"users"}"""
    user_name = f"""{message.from_user.username}"""
    new_directory(user_directiry, user_name)

    drive = google_drive()
    file_name = drive.download(file_id=file_id, file_name=f"""users/{user_name}/{"table"}.csv""")
    json = csv_table(file_name)
    photo = json_convert(json, user_name=user_name)
    print(photo)
    await message.reply_photo(photo=types.InputFile(photo))


if __name__ == '__main__':
    while True:
        print('start')
        executor.start_polling(dp)
