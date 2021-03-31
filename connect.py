"""import telebot
bot = telebot.TeleBot('1696360118:AAG6Z-R627A2GefoHgk8mmmjmbee5xS8f4o')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling()"""

# доделаю в другой раз