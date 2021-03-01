from aiogram import types
from misc import dp,bot
import asyncio



#{"id": -1001261024756, "title": "Отзывы", "username": "qwmoneyrewiews", "type": "channel", "invite_link": "https://t.me/joinchat/Sym19CIfHDxLoOpj"}

@dp.message_handler(content_types='text')
async def all_other_messages(message: types.message):
    print(message.chat.id)