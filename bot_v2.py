import telebot
import requests
import shutil
bot = telebot.TeleBot('5916023815:AAHb_7-LdkQNPR61OtiLafeGumAAROMb5nY') 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Могу скинуть кота,надо?")
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    user_text=message.text
    if (user_text=="Да") or (user_text=="да"):
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
        bot.send_photo(message.chat.id, url,)
        bot.send_message(message.chat.id, "Еще кота?")
    elif (user_text=="Нет") or (user_text=="нет"):
        bot.send_message(message.chat.id, "На нет и суда нет")
bot.polling(non_stop=True)