# -*- coding: utf-8 -*-
import requests
import os, time
access_token = ""
def del_album():
    #vk_id = "67267231" # skynet
    vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/photos.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    for G in data['response']['items']:
        if G['title'] != "СХЕМЫ":
            #print(G['title'], G['id'])
            URL1 = f"https://api.vk.com/method/photos.deleteAlbum?group_id={vk_id}&access_token={access_token}&v=5.92&album_id={G['id']}"
            r = requests.get(url = URL1).json() 
            print (r)
            time.sleep(0.5)

def del_videos():
    vk_id = "67267231" # skynet
    #vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/video.get?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    print (data)
    for G in data['response']['items']:
        print (G["id"])        
        URL1 = f"https://api.vk.com/method/video.delete?owner_id=-{vk_id}&access_token={access_token}&v=5.92&video_id={G['id']}"
        r = requests.get(url = URL1).json() 
        print (r)
        time.sleep(0.5)

del_videos()
