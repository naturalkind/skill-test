# -*- coding: utf-8 -*-
import json
import time
import matplotlib 
import matplotlib.pyplot as plt 
import requests
from datetime import date, timedelta, datetime

# Temp data base

chat_ID = "-1001478906055" 
acc_key = "1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0" 
#Inline key

def send_function():
                 op = "<strong>/list</strong> - курс валют за последние 10 минут\n"
                 op += "<strong>/exc</strong> - калькулятор валют\n"
                 op += "Пример: <strong>/exc</strong> XX.XX USD to RUB, где XX.XX - ваша сумма\n"
                 op += "<strong>/hist</strong> - график валют по отношнию друг к другу\n"
                 op += "Пример: <strong>/hist</strong> USD RUB X - где X колличество дней"
#                 {
#                        "chat_id": "123456",
#                        "text": "Hi",
#                        "reply_markup": {
#                            "inline_keyboard": [[
#                                {
#                                    "text": "A",
#                                    "callback_data": "/help"            
#                                }, 
#                                {
#                                    "text": "B",
#                                    "callback_data": "C1"            
#                                }]]
#                        }
#                    }
                      
                 BT = {"inline_keyboard": [
                                [{
                                    "text": "ardor.minbashi.com",
                                    "url":"http://ardor.minbashi.com/"
                                }],
                                [{
                                    "text": "Продолжить, мне 18",
                                    "callback_data": "age"
                                }],
                                [{
                                    "text": "Изменить на EN",
                                    "callback_data": "A1"
                                }],
                                [{
                                    "text": "◀ ", #\xE2\x97\x80
                                    "callback_data": "left"
                                },
                                {
                                    "text": "\xF0\x9F\x92\xAC", #\xF0\x9F\x92\xAC
                                    "callback_data": "lang"            
                                },
                                {
                                    "text": " ▶", #\xE2\x96\xB6
                                    "callback_data": "right"            
                                }],
                                [{
                                    "text": "Покинуть игру",
                                    "callback_data": "endgame"                                   
                                }]]}   
                 BT = json.dumps(BT)  
                 #print (BT)    
                 params = {'chat_id': chat_ID, 'text': "Hellow", "reply_markup":BT, "parse_mode":'HTML'}
                 #s_data = json.dumps(data)     
                 print (params)   
                 my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/sendMessage"
                 #r = requests.get(my_l, data)
                 
                 r = requests.get(my_l, data=params).json()
                 print ("RESEND", r)
             

send_function()            
        
# Очистка сообщений
# Кнопки:
#  передача данных, кнопка перехода на url
#  передача номера телефоноа
#  передача геолокации       
# Уметь выводить информацию в активные сообщения не удаляем а обновляем (edit)
# Выводить инфомации в несколько активных сообщений
# Ограничения по количество сообщений
#https://proglib.io/p/telegram-bot
#https://tg.sean.taipei/payload.php?sendPhoto-8c60e9bd
#https://www.mindk.com/blog/how-to-develop-a-chat-bot/
#https://apps.timwhitlock.info/emoji/tables/unicode
                                

        
                      

