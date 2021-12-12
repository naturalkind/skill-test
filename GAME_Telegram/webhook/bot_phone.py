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
                 BT = {"keyboard": [[{"text": "Кнопка1", "request_contact": True}]],
                      } 
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

#https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html
#https://qna.habr.com/q/524819                                
#https://qna.habr.com/q/465051
        
#https://pythonru.com/primery/python-telegram-bot

#https://github.com/yagop/node-telegram-bot-api/issues/108                     
#https://tutorials.botsfloor.com/request-and-handle-phone-number-and-location-with-telegram-bot-api-e90004c0c87e
#https://github.com/TelegramBots/telegram.bot/issues/198
