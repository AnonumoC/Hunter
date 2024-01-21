import builtins
import telebot

bot = telebot.TeleBot('6604654358:AAGO76LEH2d5QbfG9F0UalT1-gC3VBHuhHQ')

@bot.message_handler(func=lambda message: True, content_types=['start'])

def start(message):
    bot.reply_to(message, "Welcome to the group!")
    bot.send_message(message.chat.id, ('salom'))

bot.polling()
