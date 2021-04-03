# -*- coding: utf-8 -*-
import requests
import os
vk_id = "67267231"
vk_id2 = "47376425"
access_token = "261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8"
URL = f"https://api.vk.com/method/photos.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"

r = requests.get(url = URL) 
data = r.json() 
for G in data['response']['items']:
    print(G['title'])
    URL1 = f"https://api.vk.com/method/photos.createAlbum?group_id={vk_id2}&access_token={access_token}&v=5.92&title={G['title']}&upload_by_admins_only=1"
    r = requests.get(url = URL1).json() 
    print (r)
