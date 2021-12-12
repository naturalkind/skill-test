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

#def send_function():
#                 params = {'chat_id': chat_ID}
#                 #s_data = json.dumps(data)     
#                 my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/deleteMessage"
#                 
#                 r = requests.get(my_l, data=params).json()
#                 print ("RESEND", r)
#   

#def del_mess(x):
#                 params = {'chat_id': chat_ID, 'message_id':x, 'can_delete_messages':True}
#                 #s_data = json.dumps(data)     
#                 my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/promoteChatMember"#"deleteMessage"
#                 
#                 r = requests.post(my_l, data=params).json()
#                 print ("RESEND", r)          

def del_mess(x):
                 params = {'chat_id': chat_ID, 'message_id':x}
                 print (params)    
                 my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/deleteMessage"
                 
                 r = requests.post(my_l, data=params).json()
                 print ("RESEND", r)
             
#send_function()  
def send_function():
                 params = {'chat_id': chat_ID}
                 #s_data = json.dumps(data)     
                 my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/getUpdates"
                 
                 r = requests.get(my_l, data=params).json()
                 key_h = r["result"]#[0]
                 #print (key_h)
                 for mes in key_h:
                     del_mess(mes["message"]["message_id"])
                     #print (mes["message"])
                 #print ("RESEND", key_h)
             

send_function()  

#getHistory         
        
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

#https://stackoverflow.com/questions/35269776/telegram-bot-how-to-delete-or-remove-a-message-or-media-from-a-channel-or-group/35271942 
#DELITE
                                
