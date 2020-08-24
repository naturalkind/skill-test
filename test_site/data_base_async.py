#!/usr/bin/env python3

import os
import json

from motor.motor_tornado import MotorClient
import tornado.web
import tornado.ioloop
import tornado.websocket
import asyncio
from bson.objectid import ObjectId

#ws://178.158.131.41:8800/websocket
MONGO_HOST = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
LISTEN_PORT = int(os.environ.get("LISTEN_PORT", 8800))
MESSAGES_SHOW_LIMIT = 10
db = MotorClient(MONGO_HOST, MONGO_PORT)["telegram"]

async def get():
        cursor = db["messages"].find().sort('_id', -1).limit(MESSAGES_SHOW_LIMIT)
        C = await db["messages"].find().count()
        messages = await cursor.to_list(None)
        messages.reverse()
        print (messages, len(messages), C)
        
        
tornado.ioloop.IOLoop.current().run_sync(get)

####### DEL ONE & POST ONE--->
#idx = "5e50162ab2c79a45c3403dee"
#async def f_one():
#                 result = await db["messages"].find_one({"_id":ObjectId(idx)})
#                 return result
#                 #result = await db["messages"].delete_one(result)
#                 #result.deleted_count 
#async def del_one():
#                 result = await f_one()
#                 print (result)
#                 if result != None:
#                         result = await db["messages"].delete_one(result)
#                         result.deleted_count

#tornado.ioloop.IOLoop.current().run_sync(del_one)

####### DEL ALL --->

#async def del_all():
#        C = await db["messages"].delete_many({}) 
#        print (C)

#tornado.ioloop.IOLoop.current().run_sync(del_all)

#######################
####### ADD USR --->

#post = {'user': "name", 'text': ' asas'}
#async def add_user():
#        post_id = await db["messages"].insert_one(post)#.inserted_id
#        print (post_id.inserted_id)

#tornado.ioloop.IOLoop.current().run_sync(add_user)

#######################
####### UPDATE ONE --->

#post = {'user': "name", 'text': ' AAAA'}
#async def update_user():
#        post_id = await db["messages"].update_one({"user" : "name"},
#                                               {"$set": post}, upsert=True)
#        print (post_id)

#tornado.ioloop.IOLoop.current().run_sync(update_user)

#######################
####### UPDATE MANY --->

#post = {'user': "name", 'text': ' AAAA'}
#async def update_user():
#        post_id = await db["messages"].update_many({"user" : "name"},
#                                               {"$set": post}, upsert=True)
#        print (post_id)

#tornado.ioloop.IOLoop.current().run_sync(update_user)

#######################
