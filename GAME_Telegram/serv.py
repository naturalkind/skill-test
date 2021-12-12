import random
import time
import tornado.ioloop
import tornado.web
import json
import base64
import cv2
import os, sys
import numpy
import time
import io
import requests

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="Нейронная сеть/Тренировка")
    def post(self):
        self.set_header("Content-Type", "application/json")
        data_json = json.loads(self.request.body)
        print ("OK")
                         
              

         

		
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8800, address='192.168.1.50')
    tornado.ioloop.IOLoop.current().start()
     



