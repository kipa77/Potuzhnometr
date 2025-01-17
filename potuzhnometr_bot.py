import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7243122835:AAGgYp2mNsUlzfmenXa-KF9QiS-xKIZwkww')


dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Відкрити застосунок',web_app=WebAppInfo(url='https://kipa77.github.io/Potuzhnometr/')))
    await message.answer('Жми знизу',reply_markup=markup)

executor.start_polling(dp)
