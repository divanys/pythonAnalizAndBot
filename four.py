import telebot
from telebot import types
from time import sleep
import random
from tokenBot import TOKEN  # шобэ никто не спалил и не накосячил

bot = telebot.TeleBot(TOKEN)


# start
@bot.message_handler(commands=['start'])
def randomNum(mess):
    num = random.randint(-100, 100)
    bot.send_message(mess.chat.id, f'hello?{str(num)}\n//cheKak')

@bot.message_handler(content_types=['text'])
def cheKak(mess):
    with open('file', 'a') as f:
        enter111 = str(mess.text) + '\n'
        f.write(enter111)
    bot.send_message(mess.chat.id, enter111)
bot.polling()
