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
import threading
import asyncio
import websockets


               
async def hello():
    uri = "ws://178.158.131.41:8800/websocket"
    async with websockets.connect(uri) as websocket:
        #name = input("What's your name? ")
        while True:
                name = "Vipol"
                mess = json.dumps({'user': name, 'text': ' asas'})
                await websocket.send(mess)
                time.sleep(0.01)



asyncio.get_event_loop().run_until_complete(hello())




