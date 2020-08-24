#!/usr/bin/env python3

import os
import json

from motor.motor_tornado import MotorClient
import tornado.web
import tornado.ioloop
import tornado.websocket
import asyncio

#ws://178.158.131.41:8800/websocket
MONGO_HOST = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
LISTEN_PORT = int(os.environ.get("LISTEN_PORT", 8800))
MESSAGES_SHOW_LIMIT = 10
db = MotorClient(MONGO_HOST, MONGO_PORT).telegram

async def get():
        cursor = db.messages.find().sort('_id', -1).limit(MESSAGES_SHOW_LIMIT)
        C = await db.messages.find().count()
        messages = await cursor.to_list(None)
        messages.reverse()
        print (messages, len(messages), C)
        
        
tornado.ioloop.IOLoop.current().run_sync(get)

####### ADD USR --->

#post = {'user': "name", 'text': ' asas'}
#async def add_user():
#        post_id = await db.messages.insert_one(post)#.inserted_id
#        print (post_id.inserted_id)

#tornado.ioloop.IOLoop.current().run_sync(add_user)

#######################

post = {'user': "name", 'text': ' asas'}
async def del_user():
        post_id = await db.messages.insert_one(post)#.inserted_id
        print (post_id.inserted_id)

tornado.ioloop.IOLoop.current().run_sync(add_user)
