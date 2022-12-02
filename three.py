import telebot
from selenium import webdriver
from time import sleep


TOKEN = '5957678394:AAGiRrqXLwwx3yuNtX1b4YtvrfmtPfD2mmM'
bot = telebot.TeleBot(TOKEN)

driver = webdriver.Chrome()
@bot.message_handler(commands=['start'])
def start(mess):
    bot.send_message(mess.chat.id, 'Привет! Я парсер-бот :)')



@bot.message_handler(commands=['searchVideos'])
def searchVideos(mess):
    msg = bot.send_message(mess.chat.id, 'ван сек, введи текст, я найду в ютубчике')
    bot.register_next_step_handler(msg, search)

@bot.message_handler(content_types=['text'])
def text(mess):
    bot.send_message(mess.chat.id, 'че хочш? ')
def search(mess):
    bot.send_message(mess.chat.id, 'Начинаю искать, сладенький)))))))')
    searchVideo = 'https://www.youtube.com/results?search_query=' + mess.text
    driver.get(searchVideo)
    sleep(2)

    videos = driver.find_elements('thumbnail')
    for i in range(len(videos)):
        bot.send_message(mess.chat.id, videos[i].get_attribite('href'))

bot.polling()