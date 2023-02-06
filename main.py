import asyncio
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import logging
import os

load_dotenv()

# BOT_TOKEN = secrets.BOT_TOKEN
# BOT_TOKEN = '6095088518:AAFKVIpJqGLaWJLyNDGp8L2SHhjLToBvE9w'
BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')

# text = "Важно!! 🧨 \nУ нас обязательный опросник (3 вопроса). \n 🎫 Все участники должны его заполнить или бот автоматически кикнет из группы в течении 24 часов. Напиши '+' без кавычик чтобы пройти. \nHi there! What's your name?"

print(f'Initializing bot with {BOT_TOKEN=} ...')

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
#  Диспетчер
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer("Привет, как дела?")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("У меня всё хорошо, спасибо что спросил")

#
# Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

