# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import json
import base64
import cv2
import os, sys
import numpy
import time
import io
#from tornado.escape import json_encode
import matplotlib 
import matplotlib.pyplot as plt 
import requests
from datetime import date, timedelta, datetime
#from data_base import mDB

#db = mDB()
temp_ch_db = {}
temp_ch_db["time"] = int(time.time())
temp_ch_db["data"] = 0

#txt = "привет я андроид наташа, не обзывай хозяина"
def get_ls():
        my_l = "https://api.exchangeratesapi.io/latest?base=USD"
        r = requests.get(my_l)
        G = json.loads(r.text)
        print type(G), G

        H = G["rates"]
        dict = {}
        for i in H.keys():
            #print i, round(H[i],2)#float("{0:.2f}".format(H[i]))#H[i]
            dict[i] = round(H[i],2)
        return dict
#print get_ls()         


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
                         
                 
                 my_l = "https://api.telegram.org/bot1073537741:AAFObWjiUeUhzlz6HdkR_gT4cAnvyXcQepU/sendMessage?chat_id=-321132488&text="+str(op)+"&parse_mode=html"
                 r = requests.get(my_l)
                 #G = json.loads(r.text)
                 
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
                 #print H[s_out], f_out #, s_vin, s_vout, f_out
                 my_l = "https://api.telegram.org/bot1073537741:AAFObWjiUeUhzlz6HdkR_gT4cAnvyXcQepU/sendMessage?chat_id=-321132488&text="+str(round(f_out,2))+"&parse_mode=html"
                 r = requests.get(my_l)
                 
              ######################   
              if s_sp[0] == "/list": 
               
                   #print data_json
                   S_time = int(time.time())
                   #temp_ch_db["time"] = obj
                   new_st = (S_time - temp_ch_db["time"])
                   print new_st, temp_ch_db["time"]
                   if new_st == 3600 or new_st <= 0:
                        obj = get_ls()
                        temp_ch_db["time"] = S_time
                        temp_ch_db["data"] = obj
                        print "Start or 10min"
                   else: 
                        obj = temp_ch_db["data"]  
                        print "Non 10min"
                   #print obj, temp_ch_db["data"], temp_ch_db["time"], new_st
                   op = "<strong>Курс валют " + str(end) + "</strong>\n"
                   
#                   S_time = time.ctime()
#                   S_time = S_time.split(" ")[-2]
#                   S_time = [int(x) for x in S_time.split(":")]
                   
                   #S_time = time.time()
                   
                   
                   for R in obj.keys():
                       #print obj[R]
                       op += str(R) +": "+str(obj[R])+"\n"
                   my_l = "https://api.telegram.org/bot1073537741:AAFObWjiUeUhzlz6HdkR_gT4cAnvyXcQepU/sendMessage?chat_id=-321132488&text="+op+"&parse_mode=html"
                   r = requests.get(my_l)
                   
              ##########################     
              if s_sp[0] == "/hist":
              
                    s_base = str(s_sp[1])
                    s_out = str(s_sp[2])
                    d_as = int(s_sp[-1])
                    start = end - timedelta(days=d_as)#12)
                    graph_exch = "https://api.exchangeratesapi.io/history?start_at="+str(start)+"&end_at="+str(end)+"&base="+s_base +"&symbols="+ s_out#CAD
                    r = requests.get(graph_exch)
                    G = json.loads(r.text)  
                    #print type(G), G
                    G = G["rates"]
                    x = []
                    y = [] 
                    for ix, o in enumerate(G):
                            #print o, G[o][G[o].keys()[0]] #G[o]
                            tmp=str(o).split("-")
                            #print tmp
                            x.append(ix) # matplotlib.dates.date2num(tmp[-1])datetime.strptime(tmp, '%Y%m%d')
                            y.append(G[o][G[o].keys()[0]])  
                    fig, ax = plt.subplots()
                    ymax = max(y)

                    xmax = x[y.index(ymax)]

                    ymax=round(ymax,2) #округляем максимум до копеек.
                    ax.annotate('MAX:'+str(ymax), #на график поместим аннотацию: максимальное значение доллара.
	                         xy=(xmax, ymax*(1.005)), #место куда поместим аннотацию: визуально чуть-чуть повыше максимума. 
	                         horizontalalignment='center', #выровняем метку максимума по центру.
                               )
                    ax.plot(x, y, color="g")
                    plt.title(s_base+"/"+s_out, fontsize=20)
                    plt.grid() #наносим сетку.
                    plt.savefig('data.png') 
                    url = "https://api.telegram.org/bot1073537741:AAFObWjiUeUhzlz6HdkR_gT4cAnvyXcQepU/sendPhoto";
                    files = {'photo': open('data.png', 'rb')}
                    data = {'chat_id' : "-321132488"}
                    r= requests.post(url, files=files, data=data) 
        except KeyError:
             print "PASS"   
             
             
        
import threading

LS = "https://api.telegram.org/bot1073537741:AAFObWjiUeUhzlz6HdkR_gT4cAnvyXcQepU/getUpdates"

def thread_function():
    message_id = ""
    while True:
         #print "Start"
         r = requests.get(LS)
         G = json.loads(r.text)
         key_h = G["result"][-1].keys()[0]
         #print key_h
#         if key_h == "edited_message":
#            send_function(G["result"][-1][key_h]) 
#            message_id = G["result"][-1][key_h]["message_id"]
         if message_id != G["result"][-1][key_h]["message_id"]:
            send_function(G["result"][-1][key_h]) 
            message_id = G["result"][-1][key_h]["message_id"]
          
threads = []
x = threading.Thread(target=thread_function)
threads.append(x)
x.start()                                    

