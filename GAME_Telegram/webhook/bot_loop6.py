# -*- coding: utf-8 -*-
import json
import time
import requests
from datetime import date, timedelta, datetime


acc_key = "1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk" 
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

def edit_Key(chat_ID, mesg_ID, x):
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
                 MES = "Вы нажали кнопку: "+str(x)
                 params = {'chat_id': chat_ID, 'message_id':mesg_ID, 'text':MES, "reply_markup":json.dumps(BT), "parse_mode":'HTML'}
                 #print (params)    
                 my_l = "https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/editMessageText"
                 r = requests.post(my_l, data=params).json()
                 #print ("edit_mess", r,  "\n")
                 
class TempDataUser():
#{'update_id': 474903633, 
#'message': 
#       {'message_id': 382, 
#        'from': {'id': 603789567, 'is_bot': False, 'first_name': 'Victor', 'username': 'EvilSadko', 'language_code': 'ru'},
#        'chat': {'id': 603789567, 'first_name': 'Victor', 'username': 'EvilSadko', 'type': 'private'}, 
#        'date': 1586940025, 
#        'text': '/start', 
#        'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]
#       }
#}
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
         #self.username = x["message"]["from"]["username"]
         #self.first_name = x["message"]["from"]["first_name"]
         self.text = x["message"]["text"]
     def delete(self, x):
         self.DEL = x["ok"]
         
         
         
class TempDataBot():
#{'message_id': 391, 
# 'from': {'id': 1227859397, 
#          'is_bot': True, 
#          'first_name': 'bot_game_ai', 
#          'username': 'AIdifferentBot'}, 
#  'chat': {'id': 603789567, 
#           'first_name': 'Victor', 
#           'username': 'EvilSadko', 
#           'type': 'private'}, 
#   'date': 1586941335, 
#   'text': 'Добрый день!\nEvilSadko'}
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

#{'update_id': 474903679, 
#'callback_query': {'id': '2593256445815025007', 
#                   'from': {'id': 603789567, 'is_bot': False, 'first_name': 'Victor', 'username': 'EvilSadko', 'language_code': 'ru'}, 
#                    'message': {'message_id': 530, 'from': {'id': 1227859397, 'is_bot': True, 'first_name': 'bot_game_ai', 'username': 'AIdifferentBot'}, 
#                    'chat': {'id': 603789567, 'first_name': 'Victor', 'username': 'EvilSadko', 'type': 'private'}, 
#                    'date': 1586947317, 
#                    'edit_date': 1586947326,
#                    'text': 'Вы нажали кнопку: 16', 
#                    'reply_markup': {'inline_keyboard': 
#                                      [[{'text': 'ardor.minbashi.com', 'url': 'http://ardor.minbashi.com/'}], 
#                                       [{'text': 'Продолжить, мне 18', 'callback_data': 'age'}], 
#                                       [{'text': 'Изменить на EN', 'callback_data': 'A1'}], 
#                                       [{'text': '◀ ', 'callback_data': 'left'}, {'text': '💬', 'callback_data': 'lang'}, {'text': ' ▶', 'callback_data': 'right'}], 
#                                       [{'text': 'Покинуть игру', 'callback_data': 'endgame'}]]}}, 
#                      'chat_instance': '2863695462849496807', 
#                      'data': 'left'}}


          
while flag:
#   try:
     G = requests.get(api_upd).json()
     #print (G['result'][-1])
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
        #Key2(DBU.chat_id)
        DBB.save(Key3(DBU.chat_id))
        #print ("ELSE")
     else:  
        tryDelete(DBU.chat_id, DBU.message_id) 
     #print (DBB.chat_id, DBB.message_id, OPS)   
     #edit_Key(DBB.chat_id, DBB.message_id, OPS) 
     edit_Key(DBB.chat_id, DBB.message_id, DBU.text) 
     OPS += 1       
        
           
     
     
     #-----------------------------__>
#     DBB.save(error_send(DBU.chat_id, DBU.username))
#     tryDelete(DBB.chat_id, DBB.message_id)
#     print (DBB.message_id, DBB.chat_id, DBB.username, DBB.text)
     
     
     #DEL1 = error_send(DB.chat_id, DB.username)
     #cht_id = DEL1["chat"]["id"]
     #msg_id = DEL1["message_id"]
     #
     #print (DEL1)
            #K = tryDelete(ix["message"]["chat"]["id"], ix["message"]["message_id"])
#            print (ix, "\n")
#            if ix["message"]["text"] == '/start' and cht_id == "" and msg_id == "":
#                    K = tryDelete(ix["message"]["chat"]["id"], ix["message"]["message_id"])
#                    print (K)
#                    if K["ok"] == True:
#                       DEL1 = error_send(ix["message"]["chat"]["id"], ix["message"]["chat"]["username"])
#                       DEL2 = sendPhoto(ix["message"]["chat"]["id"]) 
#                       cht_id = 1 
#            else:
#               if cht_id == "" and msg_id == "":
#                    DEL1 = error_send(ix["message"]["chat"]["id"], ix["message"]["chat"]["username"])  
#                    cht_id = DEL1["chat"]["id"]
#                    msg_id = DEL1["message_id"]  
#                    edit_mess(DEL1["chat"]["id"],  DEL1["message_id"]) 
#               else:
#                    edit_mess(cht_id ,  msg_id)  
#                    IDX_S += 1                           
#                    else:   
#                       
#                       #cht_id = DEL1["chat"]["id"]
#                       #msg_id = DEL1["message_id"]
#                       #edit_mess(cht_id ,  msg_id) 
#                       #IDX_S += 1
##                    else:
##                       tryDelete(cht_id, msg_id)
##                       cht_id = ""
##                       msg_id = ""
##                       print(ix)
#                       if cht_id != "" and msg_id != "":  
#                         edit_mess(cht_id ,  msg_id)              
#                         
#                       else:
#                         DEL1 = error_send(ix["message"]["chat"]["id"], ix["message"]["chat"]["username"])
#                         cht_id = DEL1["chat"]["id"]
#                         msg_id = DEL1["message_id"]
#                         #DEL1 = error_send(cht_id, msg_id)   
#                       IDX_S += 1
                       
#            if OPS  == 1:    
#                    #print (ix)
#                    if cht_id == "" and msg_id == "":
#                            DEL1 = error_send(ix["message"]["chat"]["id"], ix["message"]["chat"]["username"])
#                            cht_id = DEL1["chat"]["id"]
#                            msg_id = DEL1["message_id"]
#                            DEL2 = sendPhoto(ix["message"]["chat"]["id"]) 
#                            DEL2 = DEL2["result"] 
#                            edit_mess(DEL1["chat"]["id"],  DEL1["message_id"])
#                    else:
#                            IDX_S += 1
#                            print (">>>>>>>>>>>>>",cht_id ,  msg_id)
#                            edit_mess(cht_id ,  msg_id)      
#            
                
#                    DEL1 = error_send(ix["message"]["chat"]["id"], ix["message"]["chat"]["username"])
#                    cht_id = DEL1["chat"]["id"]
#                    msg_id = DEL1["message_id"] 
#                    edit_mess(cht_id,  msg_id)                   
#                    IDX_S += 1
                    #del_mess(ix["message"]["chat"]["id"], ix["message"]["message_id"])

                    #edit_mess(DEL1["chat"]["id"],  DEL1["message_id"])
  
            #del_mess(DEL1["chat"]["id"], DEL1["message_id"])
            #---------------------------------->
            #DEL2 = error_send(ix["message"]["chat"]["id"]) 
            #edit_mess(DEL2["chat"]["id"],  DEL2["message_id"])
            #print (DEL1)
            #del_mess(DEL2["chat"]["id"], DEL2["message_id"])
