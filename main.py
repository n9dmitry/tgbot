import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

API_TOKEN = os.environ.get('TG_BOT_TOKEN')

bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# States
class Form(StatesGroup):
    confirm = State() # +
    name = State()  # Will be represented in storage as 'Form:name'
    age = State()  # Will be represented in storage as 'Form:age'
    occupation = State()  # Will be represented in storage as 'Form:occupation'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Важно!! 🧨 \nУ нас обязательный опросник (3 вопроса). \n 🎫 Все участники должны его заполнить или бот автоматически кикнет из группы в течении 24 часов. Напиши '+' без кавычик чтобы пройти.")
    await Form.next()

@dp.message_handler(state=Form.confirm)
async def confirm(message: types.Message, state: FSMContext):
    if message.text == "+":
        async with state.proxy() as data:
            data['confirm'] = message.text
        await Form.next()
        await message.reply("Всего 3 вопроса. Вопрос 1: Напишите ФИО полностью")
    else:
        await message.answer("Нет")

@dp.message_handler(state=Form.name)
async def ask1_name(message: types.Message):
    if not len(message.text.split()) >= 2 and len(message.text.split()) <= 3:
        return await message.reply("Шляпа коня")
    else:
        await Form.next()
        return await message.reply("Сколько тебе лет?")


@dp.message_handler(state=Form.age)
async def ask2_age(message: types.Message):
    try:
        if 10 < int(message.text) < 80:
            await Form.next()
            return await message.reply("Какой твой род деятельности?")
        else:
            return await message.reply("Лох")
    except:
        return await message.reply('dolboeb')

@dp.message_handler(state=Form.occupation)
async def ask3_occupation(message: types.Message):
    try:
        if len(message.text) < 150:
            await Form.next()
            return await message.reply("Ок, молодец")
        else:
            return await message.reply("Короче давай пиши")
    except:
        return await message.reply('dolboeb')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)