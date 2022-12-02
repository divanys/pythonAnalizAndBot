import telebot
from time import sleep
import random

TOKEN = '5841926270:AAFR0HaBjylZ7cdqML72d9kOF4ewadYQU1c'
bot = telebot.TeleBot(TOKEN)


# randomNum
@bot.message_handler(commands=['randomNum'])
def randomNum(mess):
    num = random.randint(-100, 100)
    bot.send_message(mess.chat.id, str(num))


# start
@bot.message_handler(commands=['start'])
def start(mess):
    bot.send_message(mess.chat.id, 'Хули надо?')


# text
@bot.message_handler(content_types=['text'])
def text(mess):
    if mess.text.lower() == 'hello':
        bot.send_message(mess.chat.id, 'Hallo mazafucker')
    else:
        bot.send_message(mess.chat.id, 'NOOOOOOOOOOOOOOOOOOOOOOOOOOB')


bot.polling()
