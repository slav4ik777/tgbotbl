import telebot
from telebot import types
from parsing import parsingbtc

from keyboard import webAppKeyboard
from keyboard import webAppKeyboard2
from webappuser import webappuser

import os

import  os 
os.environ["TB"] = "my val"

bot = telebot.TeleBot(os.getenv('TOKENBOT'))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonA  = types.KeyboardButton("Начать")
    markup.add(buttonA)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я спциальный бот для соц. сетей в телеграмме.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def twomessage(message):

    if message.text =='Начать':
        bot.reply_to(message, 'Начнём)', reply_markup=webAppKeyboard()) 

    elif message.text == '▶Далее▶':
        bot.reply_to(message, 'Окей, босс, далее)', reply_markup=webAppKeyboard2()) 

    elif message.text == '◀Назад◀':
        bot.reply_to(message, 'Окей, босс, назад)', reply_markup=webAppKeyboard())
    
    elif message.text == '◀Вернуться в главное меню▶':
        bot.reply_to(message, 'Окей, босс)', reply_markup=webAppKeyboard())

    elif message.text == 'btc':
        bot.send_message(message.chat.id, 'Курс биткойна в реальном времени')
        parsingbtc(message)

    elif message.text == 'Свой WebApp':
        bot.send_message(message.chat.id, 'вставь ссылку на сайт')

    elif message.text[0] == 'h' and message.text[1] == 't' and message.text[2] == 't' and message.text[3] == 'p':
        webappuser(message)

    elif message.text == 'ℹ️Доп инфо':
        markup2 = types.InlineKeyboardMarkup()
        menubtn1 = types.InlineKeyboardButton('📱Группа)', url= 'https://t.me/+epS_MvNUhFYxMTUy')
        menubtn2 = types.InlineKeyboardButton('📺Канал)', url= 'https://t.me/YouHubTubeCh')        
        menubtn3 = types.InlineKeyboardButton('❌Не интересно', callback_data='delete')
        menubtn4 = types.InlineKeyboardButton('✅Нажимать', url='https://youtu.be/dQw4w9WgXcQ?si=YM23TnMN56NtO3p3') 
        menubtn5 = types.InlineKeyboardButton('🆕new', callback_data='mnbtn5')
       
        markup2.row(menubtn1,menubtn2)
        markup2.row(menubtn3,menubtn4)
        markup2.row(menubtn5)
        bot.reply_to(message, 'Ты можешь вступить в группу, где можно делиться идеями, и телеграм канал)😁', reply_markup = markup2)


@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'back':
        mk0 = types.InlineKeyboardMarkup()
        menubtn1 = types.InlineKeyboardButton('📱Группа)', url= 'https://t.me/+epS_MvNUhFYxMTUy')
        menubtn2 = types.InlineKeyboardButton('📺Канал)', url= 'https://t.me/YouHubTubeCh')        
        menubtn3 = types.InlineKeyboardButton('❌Не интересно', callback_data='delete')
        menubtn4 = types.InlineKeyboardButton('✅Нажимать', url='https://youtu.be/dQw4w9WgXcQ?si=YM23TnMN56NtO3p3') 
        menubtn5 = types.InlineKeyboardButton('🆕new', callback_data='mnbtn5')
        mk0.row(menubtn1,menubtn2)
        mk0.row(menubtn3,menubtn4)
        mk0.row(menubtn5)

        bot.send_message(callback.message.chat.id, 'Ты можешь вступить в группу, где можно делиться идеями, и телеграм канал)😁', reply_markup=mk0)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


    elif callback.data == "mnbtn5":
        mk = types.InlineKeyboardMarkup()
        inbtn1 = types.InlineKeyboardButton('📺Канал)', url='https://t.me/YouHubTubeCh')
        inbtn2 = types.InlineKeyboardButton('back', callback_data='back')
        mk.row(inbtn1, inbtn2)
        bot.send_message(callback.message.chat.id, text=' Пока не знаю, для чего этот отдел😐', reply_markup=mk)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True, interval=0)







# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):

#     if message.text == "Привет":
#         bot.send_message(message.from_user.id,"Привет")
#     elif message.text == '/help':
#         bot.send_message(message.from_user.id,'Напиши "Привет"')
#     else:
#         bot.send_message(message.from_user.id, 'Моятвоянепонимат Нажми сюда -> /help')

# bot.polling(none_stop=True, interval=0)

















# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)

# if __name__ == '__main__':
#      bot.infinity_polling()