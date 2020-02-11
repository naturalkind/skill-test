# -*- coding: utf-8 -*-
import json
import time
import matplotlib 
import matplotlib.pyplot as plt 
import requests
from datetime import date, timedelta, datetime


chat_ID = "" 
acc_key = "" 

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
             print "Ops, Error", json.loads(r.text)

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
                 my_l = "https://api.telegram.org/bot1073537741:AAHMOnAD6zAdsM1E6AyPnqs3BYP3QTh0PC0/sendMessage?chat_id="+chat_ID+"&text="+str(op)+"&parse_mode=html"
                 r = requests.get(my_l)
                 
              ######################   
              if s_sp[0] == "/exc": 
                 s_num = float(s_sp[1])
                 s_base = str(s_sp[2])
                 s_out = str(s_sp[-1])
                 my_l = "https://api.exchangeratesapi.io/latest?base="+s_base
                 r = requests.get(my_l)
                 G = json.loads(r.text)
                 H = G["rates"]
                 f_out = s_num * float(H[s_out])
                 my_l = "https://api.telegram.org/bot"+acc_key+"/sendMessage?chat_id="+chat_ID+"&text="+str(round(f_out,2))+"&parse_mode=html"
                 r = requests.get(my_l)
                 
              ######################   
              if s_sp[0] == "/list": 
                   S_time = int(time.time())
                   new_st = (S_time - temp_ch_db["time"])
                   print new_st, S_time, temp_ch_db["time"]
                   #if new_st > 3600 or new_st <= 0:
                   if new_st >= 100:
                        obj = get_ls()
                        temp_ch_db["time"] = S_time
                        temp_ch_db["data"] = obj
                        print "Start or 10min"
                   else: 
                        obj = temp_ch_db["data"]  
                        print "Non 10min"
                   op = "<strong>Курс валют " + str(end) + "</strong>\n"
                   for R in obj.keys():
                       op += str(R) +": "+str(obj[R])+"\n"
                   my_l = "https://api.telegram.org/bot"+acc_key+"/sendMessage?chat_id="+chat_ID+"&text="+op+"&parse_mode=html"
                   r = requests.get(my_l)
                   
              ##########################     
              if s_sp[0] == "/hist":
                    s_base = str(s_sp[1])
                    s_out = str(s_sp[2])
                    d_as = int(s_sp[-1])
                    start = end - timedelta(days=d_as)#12)
                    graph_exch = "https://api.exchangeratesapi.io/history?start_at="+str(start)+"&end_at="+str(end)+"&base="+s_base +"&symbols="+ s_out
                    r = requests.get(graph_exch)
                    G = json.loads(r.text)  
                    G = G["rates"]
                    x = []
                    y = [] 
                    for ix, o in enumerate(G):
                            tmp=str(o).split("-")
                            x.append(ix) 
                            y.append(G[o][G[o].keys()[0]])  
                    fig, ax = plt.subplots()
                    ymax = max(y)

                    xmax = x[y.index(ymax)]

                    ymax=round(ymax,2) 
                    ax.annotate('MAX:'+str(ymax), xy=(xmax, ymax*(1.005)), horizontalalignment='center')
                    ax.plot(x, y, color="g")
                    plt.title(s_base+"/"+s_out, fontsize=20)
                    plt.grid() 
                    plt.savefig('data.png') 
                    url = "https://api.telegram.org/bot"+acc_key+"/sendPhoto";
                    files = {'photo': open('data.png', 'rb')}
                    data = {'chat_id' : chat_ID}
                    r= requests.post(url, files=files, data=data) 
                    
        except:
             print s_sp
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
     
     
