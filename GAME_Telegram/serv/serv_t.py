import tornado.httpserver
import tornado.ioloop
import tornado.web
import ssl

class getToken(tornado.web.RequestHandler):
    #print (self.request.body)
    
    def get(self):
        print ("GET")
        self.write("hello")
    def post(self):
        print ("GET")
        self.write("hello")

application = tornado.web.Application([
    (r'/', getToken),
])
#server.crt  server.key
if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain("/media/sadko/1b32d2c7-3fcf-4c94-ad20-4fb130a7a7d4/PLAYGROUND/GAME_T/serv/ssl/server.pem", "/media/sadko/1b32d2c7-3fcf-4c94-ad20-4fb130a7a7d4/PLAYGROUND/GAME_T/serv/ssl/server.key")
    context.load_verify_locations("/etc/ssl/certs/ca-certificates.crt")
    http_server = tornado.httpserver.HTTPServer(application, ssl_options=context)
#    http_server = tornado.httpserver.HTTPServer(application, ssl_options={
#        "certfile": "/media/sadko/1b32d2c7-3fcf-4c94-ad20-4fb130a7a7d4/PLAYGROUND/GAME_T/serv/ssl/server.pem",
#        "keyfile": "/media/sadko/1b32d2c7-3fcf-4c94-ad20-4fb130a7a7d4/PLAYGROUND/GAME_T/serv/ssl/server.key",
#        "ca_certs":"",
#    })
    http_server.listen(8443)
    tornado.ioloop.IOLoop.instance().start()
    
    
#curl -F "url=https://178.158.131.41:8443/" -F "@certificate=server.pem" https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/setWebhook



#openssl req -newkey rsa:2048 -sha256 -nodes -x509 -days 365 -keyout t_bot.key -out t_bot.crt -subj "/C=RU/ST=Saint-Petersburg/L=Saint-Petersburg/O=Example Inc/CN=https://178.158.131.41:8443/"

#openssl req -new -x509 -nodes -newkey rsa:1024 -keyout server.key -out server.crt -days 3650 WORK!!!!

#openssl x509 -in YOURPUBLIC.crt -out YOURPUBLIC.pem -outform PEM


#openssl req -newkey rsa:2048 -sha256 -nodes -x509 -days 365 -keyout server.key -out server.pem -subj "/C=RU/ST=Saint-Petersburg/L=Saint-Petersburg/O=Example Inc/CN=https://178.158.131.41:8443/"


#openssl req -newkey rsa:2048 -sha256 -nodes -x509 -days 365 -keyout server.key -out server.pem

#curl -F "url=https://178.158.131.41:8443/" -F "@certificate=/media/sadko/1b32d2c7-3fcf-4c94-ad20-4fb130a7a7d4/PLAYGROUND/GAME_T/serv/ssl/server.pem" https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/setWebhook

#проверка openssl x509 -text -noout -in server.pem

#curl https://api.telegram.org/bot1227859397:AAHMyk5SibE7WXo4kYc78nxCjTyCOHxQdVk/deleteWebhook


#http://178.158.131.41:8443/
