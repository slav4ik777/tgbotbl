from telebot import types

def kbuser(urll): 
   kb = types.ReplyKeyboardMarkup(resize_keyboard=True) 
   webApp = types.WebAppInfo(url=urll.text) 
   btn1 = types.KeyboardButton(text="you", web_app=webApp)

   btn2 = types.KeyboardButton("◀Вернуться в главное меню▶")
   kb.row(btn1, btn2)       

   return kb 
