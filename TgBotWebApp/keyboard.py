import telebot

from telebot import types


def webAppKeyboard(): #создание клавиатуры с webapp #
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #создаем клавиатуру


   webAppTest = types.WebAppInfo("https://trychatgpt.ru/") 
   btngpt = types.KeyboardButton(text="GPT", web_app=webAppTest)

   webAppTest = types.WebAppInfo("https://github.com/") 
   btngit = types.KeyboardButton(text="💻GitHub", web_app=webAppTest)
   keyboard.row(btngit, btngpt)

   webAppTest = types.WebAppInfo("https://www.youtube.com/?app=desktop&hl=RU&themeRefresh=1") #формат хранения url
   btn1 = types.KeyboardButton(text="📺YouTube", web_app=webAppTest) #кнопка

   webAppTest2 = types.WebAppInfo("https://vk.com/feed") 
   btn2 = types.KeyboardButton(text="📱VK", web_app=webAppTest2)

   webAppTest2 = types.WebAppInfo("https://habr.com/ru/feed/") 
   btnhab = types.KeyboardButton(text="💻Habr", web_app=webAppTest2)

   webAppTest3 = types.WebAppInfo("https://rutube.ru/") 
   btn3 = types.KeyboardButton(text="💩RuTube", web_app=webAppTest3)

   keyboard.row(btn1, btn2, btn3, btnhab) #добавляем кнопки в клавиатуру

   btn4 = types.KeyboardButton(text="ℹ️Доп инфо")

   mar2 = types.KeyboardButton("▶Далее▶")

   btcbtn = types.KeyboardButton("btc")
   keyboard.row(mar2,btcbtn,btn4)  
  

   return keyboard #возвращаем клавиатуру


def webAppKeyboard2():  
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 

   webAppTest = types.WebAppInfo("https://github.com/") 
   btn1 = types.KeyboardButton(text="💻GitHub", web_app=webAppTest)

   webAppTest2 = types.WebAppInfo("https://habr.com/ru/feed/") 
   btn2 = types.KeyboardButton(text="💻Habr", web_app=webAppTest2)

   webAppTest3 = types.WebAppInfo("https://lexica.art/") 
   btn3 = types.KeyboardButton(text="💻Lexica", web_app=webAppTest3)


   keyboard.row(btn1, btn2, btn3) 


   btn4= types.KeyboardButton(text="ℹ️Доп инфо")

   mk2 = types.KeyboardButton("◀Назад◀")

   wbappbtn = types.KeyboardButton("Свой WebApp")
   keyboard.add(mk2,wbappbtn,btn4)    

   return keyboard 