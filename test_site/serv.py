# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.websocket

import json
import base64
import cv2
import os, sys
import numpy
import time
import io
import requests
from data_base import DataBase

db_con = DataBase()

"""
User Field

User-ID
UserName
Password
Image

Chat

Mes-ID
Mes-Text
Mes-media


"""


class WebSocket(tornado.websocket.WebSocketHandler):
    clients = set()
    def open(self):
        WebSocket.clients.add(self)
        print("WebSocket opened from: " + self.request.remote_ip)
        
    def on_close(self):
        WebSocket.clients.remove(self)
        print("WebSocket closed from: " + self.request.remote_ip)

    def on_message(self, message):
        ms =  json.loads(message)
        
        ##########################
        ## Users & User
        ##########################
        if ms["Process"] == "GetUsers":
           count_u = db_con.see_count_user()
           #list_u = db_con.see_all_user()
           #x = range(0,s, 100)
           #print count_u, len(list_u), list_u[:1]
        #if ms["Process"] == "GetUser":   
        
        if ms["Process"] == "GetUser":
           count_u = db_con.see_count_user()
           #list_u = db_con.see_all_user()
           #x = range(0,s, 100)
           #print count_u, len(list_u), list_u[:1]
        #if ms["Process"] == "GetUser":   
        
        ##########################
        ## Post & Task
        ##########################         
             
           
        self.write_message(json.dumps({"Process": "MoreData"}))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
	self.render("index.html", title="Нейронная сеть/Тренировка")
    def post(self):
        ms = json.loads(self.request.body)
        print ms
        idx = db_con.get_one_user(ms["name_id"])
        if idx == None:
           print "Create New"
           db_con.user_add(ms)
           self.write(json.dumps({"Process": "Register&Exit"}))
        else:
                if idx["pass"] != ms["pass"]:
                   print "Pass Error"
                   self.write(json.dumps({"Process": "Error"})) 
                else:
                   print "Enter"
                   #idx["_id"] = str(idx["_id"])
                   strURL = "/base.html?name_id={}&text=Hellow".format(str(idx["_id"]), )
                   #self.write(json.dumps({"Process": "Exit", "URL":"/base.html", "data":idx})) 
                   self.write(json.dumps({"Process": "Exit", "URL":strURL})) 
                   #self.redirect("./robots-AI.jpg")

		
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSocket),
	(r"/(robots-AI.jpg)", tornado.web.StaticFileHandler, {'path':'./'}),
	(r"/(base.html)", tornado.web.StaticFileHandler, {'path':'./'}),
	
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8800, address='192.168.1.50') #
    #app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


