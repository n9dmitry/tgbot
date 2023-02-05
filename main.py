import telebot

TOKEN = "6095088518:AAFKVIpJqGLaWJLyNDGp8L2SHhjLToBvE9w"
bot = telebot.TeleBot(TOKEN)



# Приветствие. Опрос: фио, возраст, род занятий.

def process_survey(message):
    try:
        full_name = message.text.strip()
        msg = bot.send_message(chat_id=message.chat.id,
                               text="Сколько лет тебе?")
        bot.register_next_step_handler(msg, process_age, full_name=full_name)
    except Exception as e:
        bot.reply_to(message, 'Упс. Ошибка. Что-то не так...')

def process_age(message, full_name):
    try:
        age = message.text.strip()
        msg = bot.send_message(chat_id=message.chat.id,
                               text="Какой твой род занятий")
        bot.register_next_step_handler(msg, process_occupation, full_name=full_name, age=age)
    except Exception as e:
        bot.reply_to(message, 'Упс. Ошибка. Что-то не так...')

def process_occupation(message, full_name, age):
    try:
        occupation = message.text.strip()
        bot.send_message(chat_id=message.chat.id,
                         text="Спасибо, {}! Тебе {} лет твой род занятий {}.".format(full_name, age, occupation))
    except Exception as e:
        bot.reply_to(message, 'Упс. Ошибка. Что-то не так...')

def confirm_survey(msg):
    if msg.text.lower() == '+':
        bot.send_message(chat_id=msg.chat.id, text='Как зовут тебя, о юный отрок? (ФИО развернуто) ')
        bot.register_next_step_handler(msg, process_survey)

    else:
        bot.send_message(chat_id=msg.chat.id, text='Не верно! Напиши "+" чтобы ответить на вопросы ')
        bot.register_next_step_handler(msg, confirm_survey)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(chat_id=message.chat.id, text="Привет! Важно!!")
    bot.send_message(chat_id=message.chat.id, text="У нас обязательный опросник (3 вопроса). Все участники должны его заполнить или бот автоматически кикнет из группы в течении 24 часов. Напиши '+' без кавычик чтобы пройти ")
    bot.register_next_step_handler(message, confirm_survey)

if __name__ == "__main__":
    bot.polling()

#
