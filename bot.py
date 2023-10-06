import telebot
bot = telebot.TeleBot('Telegram token')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Start massage')
bot.polling()
