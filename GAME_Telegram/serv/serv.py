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
import matplotlib 
import matplotlib.pyplot as plt 
import requests
from datetime import date, timedelta, datetime


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="Нейронная сеть/Тренировка")
    def post(self):
        self.set_header("Content-Type", "application/json")
        start_time = time.time()
        print (self.request.body)
        #data_json = json.loads(self.request.body)


         

		
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
	(r"/(robots-AI.jpg)", tornado.web.StaticFileHandler, {'path':'./'}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8800, address='192.168.1.50') #8800
    #app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

