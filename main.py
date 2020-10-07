import telebot  # pip install pyTelegramBotAPI
import requests
import re
from telebot import types


bot = telebot.TeleBot('bot token')

@bot.message_handler(commands=['start'])
def chart(message):
    bot.send_message(message.chat.id, "OI")

def get_url(url,key):
    contents = requests.get(url).json()
    url = contents[key]
    return url    

def get_image_url(url,key):
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url(url,key)
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@bot.message_handler(commands=['bop'])
def bop(message):
    url = get_image_url('https://random.dog/woof.json','url')
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)
    
@bot.message_handler(commands=['fox'])
def fox(message):
    url = get_image_url('https://some-random-api.ml/img/fox','link')
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)

@bot.message_handler(commands=['koala'])
def fox(message):
    url = get_image_url('https://some-random-api.ml/img/koala','link')
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)


bot.polling()




