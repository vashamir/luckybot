import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = "5992712609:AAFoRvbM_8uODwZerHegUZCEiGUJU7jrQXQ" # tg_bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('Получить сигнал💸'))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.answer(text='Здравствуйте, я бот, который поможет вам стать богаче!💸 \nДля продолжения работы отправьте мне код активации')

@dp.message_handler(text=['Получить сигнал💸'])
async def give_signal(message: types.Message):
    numb = round(random.uniform(1, 5), 2)
    await message.answer(text=f'{numb}🤑', reply_markup=kb)

@dp.message_handler()
async def process_message(message: types.Message):
    msgtxt = message.text
    if msgtxt=='GaUm48gO3gk6PYhF2i8':
        await message.answer(text="Доступ получен \nПриятного пользования🤑", reply_markup=kb)
    else:
        await message.answer(text='❌Неверно!❌ \nОтправьте корректный код активации')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)