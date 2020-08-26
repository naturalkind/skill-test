import tornado.httpserver
import tornado.ioloop
import tornado.web
import ssl
import json
import time
import requests as R
import numpy as np
import cv2
import random
import os

acc_key = ""
class Telegram(tornado.web.RequestHandler):
    def get(self):
        print ("GET")
        self.write("hello")
    def post(self):
        data = json.loads(self.request.body)
        chat_id = data["message"]["from"]["id"]
        #text_mess = data["message"]["text"]
        print ("POST", chat_id, data)
        #files = sess.get("https://api.telegram.org/bot"+acc_key+"/getFile?file_id="+id_file)
        files = sess.get("https://api.telegram.org/file/bot"+acc_key+"/photos/file_1.jpg")
        with open("file_1.jpg", 'wb') as new_file:
            new_file.write(files.content)
        #------------------->
        #file = open("","wb")
        #file.write(files.content)
        #file.close()
        #------------------->
        
application = tornado.web.Application([
    (r'/', Telegram),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application, ssl_options={"certfile":"ssl/cert.crt",
                                                                          "keyfile":"ssl/cert.key",
                                                                          "ssl_version": ssl.PROTOCOL_TLSv1})
    http_server.listen(8443)
    tornado.ioloop.IOLoop.instance().start()
