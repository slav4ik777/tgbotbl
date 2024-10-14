import requests
from bs4 import BeautifulSoup as BS
import telebot

bot = telebot.TeleBot('7431624104:AAHoAGzY2lJ0CCvEyCv7hE-5MK3-ptPkicw')

def parsingbtc(btc):
    url = 'https://www.okx.com/ru/price/bitcoin-btc?channelid=ACE520285'        
    class_ = "index_price__VXAhl"
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    kurs = html.find(class_=class_).text
 
    # url = "https://www.okx.com/ru/markets/prices"
    # class_ = "last-price"
    # r = requests.get(url)
    # html = BS(r.text, 'html.parser')
    # kursrub = html.find(class_=class_).text


    url = 'https://www.binance.com/ru/price/bitcoin'
    class_ = "css-1bwgsh3"
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    kurs1 = html.find(class_=class_).text

    url = 'https://www.binance.com/ru/price/bitcoin/RUB'
    class_ = "css-1bwgsh3"
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    kurs1rub = html.find(class_=class_).text



    bot.send_message(btc.chat.id, "Информация с биржи Binance:\n" + str(kurs1) + "   " + str(kurs1rub) +
                      "\n" + "\n" + "Информация с биржи OKX:\n" + str(kurs) + "   ")


# def parsing(pr):
#     url = ""
#     class_ = ""
#     request = requests.get(url)
#     html = BS(request.text, 'html.parser')
#     peremennaya = html.find(class_=class_).text
#     bot.send_message(pr.chat.id, 'd' + str(peremennaya))    