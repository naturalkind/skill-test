# -*- coding: utf-8 -*-
import requests
import os, time, json

#vk_id = "67267231" # skynet
vk_id = "47376425" #цифровая копия

access_token = "261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8"
s_offset = 0
error = []
G = True
while G:
    URL = f"https://api.vk.com/method/wall.get?owner_id=-{vk_id}&count=10&offset={s_offset}0&access_token={access_token}&v=5.92"
    #offset=200 - смещение
    r = requests.get(url = URL) 
    data = r.json() 
    if len(data['response']['items']) != 0:
        for ix, h in enumerate(data['response']['items']):
            try:
                namefl = h["attachments"][0]['photo']['sizes'][-1]['url']
                p = requests.get(namefl)
                namefl = namefl.split("?")[0].split("/")[-1]
                out = open(f"{vk_id}/{namefl}", "wb")
                out.write(p.content)
                out.close()
            except KeyError:
                error.append(h)
           
        s_offset += 1
        time.sleep(1)
    else:
        G = False                
print (s_offset)
with open(f"{vk_id}_wall.json", 'w') as js_file:
    json.dump(error, js_file)   
#192
"""
p = requests.get(img)
out = open("...\img.jpg", "wb")
out.write(p.content)
out.close()
# -*- coding: utf-8 -*-

#код доступа
#bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009

#https://api.vk.com/method/users.get?
#user_ids=210700286&fields=bdate&
#access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92

import requests

#URL = "https://api.vk.com/method/users.get?user_ids=33923843&fields=bdate&access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92"
URL = "https://api.vk.com/method/wall.get?owner_id=-87891112?count=100&access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92"

#47376425 group ??
#87891112 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
data2 = data['response']
data3 = data2['items']
#print data2['items'], len(data3)#.keys()
for ix, h in enumerate(data3):
  try:
     namefl = h[u'attachments'][0]['photo']['sizes'][-1]['url']
     print "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", ix, type(h[u'attachments']), namefl.split('/')[-1]#h[u'attachments'][0]['photo']['sizes'][-1]['url']#.keys()#h.keys(), 
     p = requests.get(namefl)
     out = open(namefl.split('/')[-1], "wb")
     out.write(p.content)
     out.close()
  except KeyError:
     print "ERROR"# h.keys()


"""
#https://sysblok.ru/courses/1000-druzej-pavla-durova-kak-vykachivat-dannye-vkontakte/
