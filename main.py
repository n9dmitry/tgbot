import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import logging
import os
import secrets

load_dotenv()

BOT_TOKEN = secrets.BOT_TOKEN
# BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
print(BOT_TOKEN)

print(f'Initializing bot with {BOT_TOKEN=} ...')

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
#  Диспетчер
dp = Dispatcher(bot)


# Эхо - возвращает весь полученный текст
@dp.message_handler()
async def cmd_start(message: types.Message):
    await message.answer(message.text)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())