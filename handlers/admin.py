from aiogram import types
from misc import dp, bot
import sqlite3
import asyncio
from .sqlit import members_list

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


ADMIN_ID_1 = 494588959 #Cаня





@dp.message_handler(commands=['admin'])
async def admin_ka(message: types.Message):
    id = message.from_user.id
    if id == ADMIN_ID_1 :
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Трафик', callback_data='list_members')
        markup.add(bat_a)
        await bot.send_message(message.chat.id,'Выполнен вход в админ панель',reply_markup=markup)


@dp.callback_query_handler(text='list_members')  # АДМИН КНОПКА Рассылка пользователям
async def check_members(call: types.callback_query, state: FSMContext):
    a = members_list()
    await bot.send_message(call.message.chat.id, f'Кол-во пользователей:{a}')
