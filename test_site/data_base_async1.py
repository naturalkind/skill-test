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
#!/usr/bin/env python3

import os
import json

from motor.motor_tornado import MotorClient
import tornado.web
import tornado.ioloop
import tornado.websocket

LISTEN_PORT = int(os.environ.get("LISTEN_PORT", 8800))

class asyMongo(object):
        def __init__(self):
                self.MONGO_HOST = os.environ.get("MONGO_HOST", "127.0.0.1")
                self.MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
                self.MESSAGES_SHOW_LIMIT = 10
                self.db = MotorClient(self.MONGO_HOST, self.MONGO_PORT)["telegram"]
        async def get(self):
                cursor = self.db["messages"].find().sort('_id', -1).limit(self.MESSAGES_SHOW_LIMIT)
                messages = await cursor.to_list(None)
                messages.reverse()
                return messages
        async def add_mess(self, post):
                post_id = await db["messages"].insert_one(post)#.inserted_id
                print (post_id.inserted_id)
        
      
#tornado.ioloop.IOLoop.current().run_sync(DDD.get)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        messages = self.application.db.get()
        self.render('chat.html', messages=messages)


class WebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.application.webSocketsPool.append(self)

    def on_message(self, message):
        message_dict = json.loads(message)
        print (message_dict)
        self.application.db.add_mess(message_dict)
        for key, value in enumerate(self.application.webSocketsPool):
            if value != self:
                value.ws_connection.write_message(message)

    def on_close(self, message=None):
        for key, value in enumerate(self.application.webSocketsPool):
            if value == self:
                del self.application.webSocketsPool[key]


class Application(tornado.web.Application):
    def __init__(self):
        self.webSocketsPool = []
        self.db = asyMongo()#MotorClient(MONGO_HOST, MONGO_PORT).telegram

        handlers = (
            (r'/', MainHandler),
            (r'/websocket', WebSocket),
            #(r'/static/(.*)', tornado.web.StaticFileHandler,
            #{'path': 'static/'}),
        )
        super().__init__(handlers)


application = Application()


if __name__ == '__main__':
    application.listen(LISTEN_PORT)
    tornado.ioloop.IOLoop.instance().start()




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
