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

def get_ls():
        my_l = "https://api.exchangeratesapi.io/latest?base=USD"
        r = requests.get(my_l)
        G = json.loads(r.text)
        H = G["rates"]
        dict = {}
        for i in H.keys():
            dict[i] = round(H[i],2)
        return dict

temp_ch_db = {}
temp_ch_db["time"] = int(time.time())        
temp_ch_db["data"] = get_ls()
        
def error_send():
             op = "Вы ошиблись, /help"
             my_l = "https://api.telegram.org/bot"+acc_key+"/sendMessage?chat_id="+chat_ID+"&text="+op+"&parse_mode=html"
             r = requests.get(my_l)
             print ("Ops, Error", json.loads(r.text))

def send_function(data_json):
        start_time = time.time()
        end = date.today()
        try: 
              s_sp = data_json["text"].split(" ")
              #####################
              if s_sp[0] == "/help":
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
#                                    "callback_data": "A1"            
#                                }, 
#                                {
#                                    "text": "B",
#                                    "callback_data": "C1"            
#                                }]
#                            ]
#                        }
#                    }
                 data = {'chat_id': chat_ID, 'text': str(op), "parse_mode":"html"}
                 my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/sendMessage"
                 #my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/sendMessage?chat_id="+chat_ID+"&text="+str(op)+"&parse_mode=html"
                 r = requests.get(my_l, data)
        except:
             print (s_sp)
             error_send()
             

             
        
import threading

api_upd = "https://api.telegram.org/bot"+acc_key+"/getUpdates?timeout=1" 
#?allowed_updates=message &limit=4 &offset
flag = True
message_id = ""
while flag:
   try:
     r = requests.get(api_upd)
     G = json.loads(r.text)
     key_h = G["result"][-1].keys()[0]
     #print key_h,flag#G["result"]
     if message_id != G["result"][-1][key_h]["message_id"]:
           send_function(G["result"][-1][key_h]) 
           message_id = G["result"][-1][key_h]["message_id"]
   except KeyboardInterrupt:           
     flag = False

                                

        
                      

