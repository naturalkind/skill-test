# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.websocket
import uuid
import json
import base64
import cv2
import os, sys
import numpy
import time
import io
import requests
import string
import random

from data_base import DataBase

db_con = DataBase()

#class User():
#    self.UID
#    self.UName
#    self.UPass
#    self.UImg
#    def __init__(self, data):
#        self.UID = data["_id"]
#        self.UName = data["name_id"]
#        self.UPass = data["pass"]
        
#@tornado.web.authenticated
class WebSocket(tornado.websocket.WebSocketHandler):
    clients = set()
    myfile = file
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
           
        ##########################
        ## Message
        ##########################           
        if ms["Process"] == "SendMess":
           print "SEND MESS", ms         
        
        ##########################
        ## Post & Task
        ##########################     
        
        ##########################    
        ## Data
        ##########################
#        if self.get_secure_cookie("name_id") != None:
#                idx = db_con.get_one_user(self.get_secure_cookie("name_id"))
#                print (idx, self.get_secure_cookie("name_id"))
#                if ms["Process"] == "InFile":
#                   nameFile = str(uuid.uuid4())[:12] #nameFile+"_"+idx["_id"]
#                   idx["img_user"] = nameFile + "." +ms["Name"].split(".")[-1]
#                   db_con.upd_user(idx["_id"], idx)
#                   print "Start"
#                   self.myfile = open(idx["img_user"], "wb")
#                   self.write_message("MoreData")
#                if ms["Process"] == "Upload":
#                   da = ms["Data"]#.encode("utf-8")#
#                   da = da.split(",")[1]
#                   file_bytes = io.BytesIO(base64.b64decode(da)).read()
#                   self.myfile.write(file_bytes)
#                   self.write_message("MoreData")
#                if ms["Process"]== "Done":
#                   print "Done"
#                   self.myfile.close()      
           
        #self.write_message(json.dumps({"Process": "MoreData"}))



class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("name_id")

def generateRandomString(length):
    s = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return str(''.join(random.sample(s, length)))

class RegHandler(BaseHandler):
    def get(self):
           if self.get_secure_cookie("name_id") != None:
               self.render("base.html", title="Нейронная сеть/Тренировка")
           else:
               self.render("index.html", title="Нейронная сеть/Тренировка")
               
               
# Test           
class UPHandler(BaseHandler):           
	def get(self): 
	   self.render("upload.html", title="Нейронная сеть/Тренировка") 


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):   
        #print self.get_secure_cookie("username")   
        if self.request.uri == "/base":
           try:
                   idx = db_con.get_one_user(self.get_secure_cookie("name_id"))
                   items = {"uid": str(idx["_id"]), "name_id": idx["name_id"] ,"img_user": idx["img_user"]}
           except KeyError:
                   items = {"uid": str(idx["_id"]), "name_id": idx["name_id"] ,"img_user": "None"}       
           
	   self.render("base.html", title="Нейронная сеть/Тренировка", items=json.dumps(items))
	if self.request.uri == "/chat":
	   self.render("chat.html", title="Нейронная сеть/Тренировка")   
	if self.request.uri == "/exit":
	   self.clear_cookie("name_id")
	   self.redirect("/")
#	if self.request.uri == "/upload":
#	   self.render("upload.html", title="Нейронная сеть/Тренировка")    
	   #self.render("index.html", title="Нейронная сеть/Тренировка")   	   
	
class PostHandler(BaseHandler):
    def post(self):
        ms = json.loads(self.request.body)
        print ms
        idx = db_con.get_one_user(ms["name_id"])
        if idx == None:
           print "Create New"
           db_con.user_add(ms)
           self.write(json.dumps({"Process":"Register&Exit"}))
        else:
                if idx["pass"] != ms["pass"]:
                   print "Pass Error"
                   self.write(json.dumps({"Process": "Error"})) 
                else:
                   print "Enter"
                   #idx["_id"] = str(idx["_id"])
                   #strURL = "/base?name_id={}&text=Hellow".format(str(idx["_id"]), )
                   strURL = "/base"
                   #self.write(json.dumps({"Process": "Exit", "URL":"/base.html", "data":idx}))
                   self.set_secure_cookie("name_id",ms["name_id"]) 
                   self.write(json.dumps({"Process": "Exit", "URL":strURL})) 

		
def make_app():
    settings = {
        "cookie_secret": generateRandomString(50),
        "login_url": "/",
    }
    return tornado.web.Application([
        (r"/", RegHandler),
        #(r"/in", RegHandler)
        (r"/base", MainHandler), 
        (r"/chat", MainHandler),
        (r"/exit", MainHandler),
        (r"/upload", UPHandler),#MainHandler),
        (r"/websocket", WebSocket),
        (r"/post", PostHandler),
	(r"/(robots-AI.jpg)", tornado.web.StaticFileHandler, {'path':'./'}),
	#(r"/(base.html)", tornado.web.StaticFileHandler, {'path':'./'}),
	
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8800, address='192.168.1.50') #
    #app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# Доабавить свои 5 ком
# Почему Django
# Техническая часть без фронта - это 
# 

            
# Путь к медиа пользователей
# Это его ID, ID - Image
# Альбом - User-ID -> AlbomID -> Image-ID
# Вывод в WEB -> www/User-ID/Image-ID
# Содать самую большую сеть картинок релевантного контента для меня!!!
# Сеть обучаеться и подбирает для меня
# Медецинское направление создание умного доктора
# Фото ==  результаты анализов
"""
Сохранять только контент
Общение без сохранения

JSON
Image

{
  ID:
  NAME_for_web:
  text:
}

User Field

{
        User-ID
        UserName
        Password
        Image: ID
}

Chat
{
Mes-ID
Mes-Text
Mes-media
}

Friend
{

}
"""    
    



