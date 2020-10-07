import telebot  # pip install pyTelegramBotAPI
import requests
import re
from telebot import types


bot = telebot.TeleBot('856966669:AAF4IAZNea21VgxQyjsi4sexqxHdnPs3898')

@bot.message_handler(commands=['start'])
def chart(message):
    bot.send_message(message.chat.id, "OI")

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_fox_url():
    contents = requests.get('https://some-random-api.ml/img/fox').json()
    link = contents['link']
    return link



def get_koala_url():
    contents = requests.get('https://some-random-api.ml/img/koala').json()
    link = contents['link']
    return link

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_fox_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_fox_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


def get_koala_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_koala_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@bot.message_handler(commands=['bop'])
def bop(message):
    url = get_image_url()
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)
    
@bot.message_handler(commands=['fox'])
def fox(message):
    url = get_fox_image_url()
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)

@bot.message_handler(commands=['koala'])
def koala(message):
    url = get_koala_image_url()
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)
    

bot.polling()




