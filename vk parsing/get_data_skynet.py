# -*- coding: utf-8 -*-
import requests
import os, time
access_token = ""
vk_id = "67267231" # skynet
#vk_id = "47376425" #цифровая копия
URL = f"https://api.vk.com/method/photos.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
r = requests.get(url = URL) 
data = r.json() 
#print (data)
for G in data['response']['items']:
    os.mkdir(f"VK/{G['title']}")
    URL_get = f"https://api.vk.com/method/photos.get?owner_id=-{vk_id}&album_id={G['id']}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL_get).json() 
    for o in r['response']['items']:
        name_save = o['sizes'][-1]['url'].split("?")[0].split("/")[-1]
        namefl = o['sizes'][-1]['url']
        p = requests.get(namefl)
        out = open(f"VK/{G['title']}/{name_save}", "wb")
        out.write(p.content)
        out.close() 
        time.sleep(0.5)

