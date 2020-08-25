# -*- coding: utf-8 -*-
import requests

#openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ssl/cert.key -out ssl/cert.crt
acc_key = "" 
files = {'certificate': open('ssl/cert.crt', 'rb')}

#------------------------->
my_l = "https://api.telegram.org/bot"+acc_key+"/setWebhook?url=https://178.158.131.41:8443"
r = requests.post(my_l, files=files)
print (r.text)
#---------------->
my_l = "https://api.telegram.org/bot"+acc_key+"/getWebhookInfo"
r = requests.get(my_l)
print (r.text)
#---------------->
#DELETE
#my_l = "https://api.telegram.org/bot"+acc_key+"/deleteWebhook"
#r = requests.get(my_l)
#print (r.text)
  



