import telebot

bot = telebot.TeleBot('6095088518:AAFKVIpJqGLaWJLyNDGp8L2SHhjLToBvE9w')

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.reply_to(message, "Hello!")

bot.polling()