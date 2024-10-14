import telebot
from kbuser import kbuser

bot = telebot.TeleBot('7431624104:AAHoAGzY2lJ0CCvEyCv7hE-5MK3-ptPkicw')

def webappuser(url):
    bot.send_message(url.chat.id, "pognali", reply_markup=kbuser(url))

