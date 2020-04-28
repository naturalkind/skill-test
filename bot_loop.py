# -*- coding: utf-8 -*-
import json
import time
import requests
from datetime import date, timedelta, datetime
from fight_config import *

acc_key = "" 
IDX_S = 0
def del_mess(chat_ID, x):
                 params = {'chat_id': chat_ID, 'message_id':x}
                 #print (params)    
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/deleteMessage"
                 r = requests.post(my_l, data=params).json()
                 print ("RESEND", r,  "\n")
        

def edit_mess(chat_ID, x):
                 MES = "Запросы с сервера "+str(IDX_S)
                 params = {'chat_id': chat_ID, 'message_id':x, 'text':MES}
                 #print (params)    
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/editMessageText"
                 r = requests.post(my_l, data=params).json()
                 print ("edit_mess", r,  "\n")
        
def error_send(chat_ID, U_NAME):
             op = "Добрый день!\n"
             op += "{}\n".format(U_NAME)
             params = {'chat_id': chat_ID, 'text':op, "parse_mode":'HTML'}
             my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/sendMessage"
             r = requests.get(my_l, data=params).json()
             #print ("Ops, Error", r,  "\n")
             return r['result']
   
def sendPhoto(chat_ID):
     my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/sendPhoto"
     files = {'photo': open('robots-AI.jpg', 'rb')}  
     params = {'chat_id' : chat_ID, 'caption':'Начнем играть?', "parse_mode":"html"}
     r= requests.post(my_l, files=files, data=params).json()
     #print(r)
     return r 
             
def get_me():
     my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/getMe"           
     r = requests.get(my_l).json()
     print ("Ops, Error", r,  "\n")
     
def get_chat(chat_ID):
     params = {'chat_id': chat_ID}
     my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/getChat"           
     r = requests.get(my_l, data=params).json()
     print ("Ops, Error", r,  "\n")     
     
def tryDelete(chat_ID, x):
     params = {'chat_id': chat_ID, 'message_id':x}
     my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/deleteMessage"
     r = requests.post(my_l, data=params).json()
     #print (r)
     return r
     
def sendLocation(chat_ID):
     params = {'chat_id': chat_ID}
     my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/sendLocation"
     r = requests.post(my_l, data=params).json()
     #print ("RESEND", r,  "\n")
     return r     


def Key1(chat_ID):
                 BT = {"keyboard": [[{"text": "Кнопка1"}]],
                       "one_time_keyboard":True,
                       "resize_keyboard":True
                      } 
                 BT = json.dumps(BT)  
                 params = {'chat_id': chat_ID, 'text': "Hellow", "reply_markup":BT, "parse_mode":'HTML'}
                 #print (params)   
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/sendMessage"
                 r = requests.get(my_l, data=params).json()
                 print ("RESEND", r)
                 
def Key2(chat_ID):
                 BT = {"ReplyKeyboardMarkup":{"keyboard":[[{"KeyboardButton":{"text":"test"}}]]}}  
                 BT = json.dumps(BT)  
                 params = {'chat_id': chat_ID, 'text': "Hellow", "reply_markup":BT, "parse_mode":'HTML'}
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/sendMessage"
                 r = requests.get(my_l, data=params).json()
                 print ("RESEND", r)                 
     
def Key3(chat_ID, op = "Тест кнопок\n"):
                 BT = {"inline_keyboard": [
                                [{
                                    "text": "ardor.minbashi.com",
                                    "url":"http://ardor.minbashi.com/"
                                }],
                                [{
                                    "text": "Продолжить, мне 18",
                                    "callback_data": "/age"
                                }],
                                [{
                                    "text": "Изменить на EN",
                                    "callback_data": "/A1"
                                }],
                                [{
                                    "text": "◀ ", #\xE2\x97\x80
                                    "callback_data": "/left"
                                },
                                {
                                    "text": "💬", #\xF0\x9F\x92\xAC
                                    "callback_data": "/lang"            
                                },
                                {
                                    "text": " ▶", #\xE2\x96\xB6
                                    "callback_data": "/right"            
                                }],
                                [{
                                    "text": "Покинуть игру",
                                    "callback_data": "/endgame"                                   
                                }]]}   
                 BT = json.dumps(BT)  
                 params = {'chat_id': chat_ID, 'text': op, "reply_markup":BT, "parse_mode":'HTML'}
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/sendMessage"
                 r = requests.get(my_l, data=params).json()
                 return r['result']
                 #print ("RESEND", r)   
                   
def KeyFight(chat_ID, op = "Удар\n"):
                 params = {'chat_id': chat_ID, 'text': op, "reply_markup":json.dumps(BT_S), "parse_mode":'HTML'}
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/sendMessage"
                 r = requests.get(my_l, data=params).json()
                 return r['result']  
                 
def edit_fight(chat_ID, mesg_ID, op = "Удар\n"):  
                 params = {'chat_id': chat_ID, 'message_id':mesg_ID, 'text': op, "reply_markup":json.dumps(BT_S), "parse_mode":'HTML'}
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/editMessageText"
                 r = requests.get(my_l, data=params).json()
                 #return r['result']                                 

def edit_Key(chat_ID, mesg_ID, x):
                 MES = "Вы нажали кнопку: "+str(x)
                 params = {'chat_id': chat_ID, 'message_id':mesg_ID, 'text':MES, "reply_markup":json.dumps(BT), "parse_mode":'HTML'}
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/editMessageText"
                 r = requests.post(my_l, data=params).json()
                 #print ("edit_mess", r,  "\n")
                 
class TempDataUser():
     data = 0
     text = 0
     message_id = 0
     chat_id = 0
     username = 0
     first_name = 0
     DEL = 0
     def __init__(self):
         pass
     def save(self, x):
         self.data = x
         self.dataParse(x)
     def dataParse(self, x):
         self.chat_id = x["message"]["chat"]["id"]
         self.message_id = x["message"]["message_id"]
         try: 
            self.username = x["message"]["from"]["username"]
         except KeyError:
            pass
         try:
            self.first_name = x["message"]["from"]["first_name"]
         except KeyError:
            pass
         self.text = x["message"]["text"]
     def delete(self, x):
         self.DEL = x["ok"]
         
         
         
class TempDataBot():
     data = 0
     text = 0
     message_id = 0
     chat_id = 0
     username = 0
     first_name = 0
     def __init__(self):
         pass
     def save(self, x):
         self.data = x
         self.dataParse(x)
     def dataParse(self, x):
         self.chat_id = x["chat"]["id"]
         self.message_id = x["message_id"]
         self.username = x["from"]["username"]
         self.first_name = x["from"]["first_name"]
         self.text = x["text"]
         
api_upd = "https://api.telegram.org/bot"+acc_key+"/getUpdates?timeout=1" 
#?allowed_updates=message &limit=4 &offset
flag = True
message_id = 0
chat_id = 0
OPS = 0         
DBU = TempDataUser()
DBB = TempDataBot()
DBB_0 = TempDataBot()
HIT_C = 0
BLOCK_C = 0
BLOCK_TYPE = 0
HIT_TYPE = 0


listHIT = ["/blockchest", "/blockbelly", "/blocklegs", "/blockhead", "/hitbelly", "/hitlegs", "/hithead" , "/hitchest"]
          
while flag:
     G = requests.get(api_upd).json()
     if G['result'] != []:
             try:
                DBU.save(G['result'][-1])
             except:
                DBU.text = G['result'][-1]['callback_query']['data']  
             if DBU.text == "/start" and DBU.DEL == 0:
                DBU.delete(tryDelete(DBU.chat_id, DBU.message_id))
             if DBU.text == "/start" and DBU.DEL == True:   
                DBB.save(error_send(DBU.chat_id, DBU.username))
                sendPhoto(DBU.chat_id)
                DBU.delete(tryDelete(DBU.chat_id, DBU.message_id))
                DBB.save(Key3(DBU.chat_id))
                DBB_0.save(KeyFight(DBU.chat_id))
             if DBU.text in listHIT:
               print (DBU.text)
               if HIT_C < 2 and DBU.text != HIT_TYPE:
                 HIT_TYPE = DBU.text
                 HIT_C += 1
                 get_BTS(DBU.text)
               if BLOCK_C < 2 and DBU.text != BLOCK_TYPE:
                 BLOCK_TYPE = DBU.text
                 BLOCK_C += 1
                 get_BTS(DBU.text)
                 #print (G['result']) 
                
             if DBU.text == "/hit":
                print ("HIT")     
             else:  
                tryDelete(DBU.chat_id, DBU.message_id) 
             edit_fight(DBB_0.chat_id, DBB_0.message_id)  
             edit_Key(DBB.chat_id, DBB.message_id, DBU.text) 
             
             OPS += 1       
                
           
