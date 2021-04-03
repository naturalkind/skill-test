# -*- coding: utf-8 -*-
import requests
import os, time
access_token = "261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8"
def get_a():
    vk_id = "67267231" # skynet
    #vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/video.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    FLINK = open("video_link.txt","w")
    for G in data['response']['items']:
        URL_get = f"https://api.vk.com/method/video.get?owner_id=-{vk_id}&album_id={G['id']}&access_token={access_token}&v=5.92"
        r = requests.get(url = URL_get).json() 
        time.sleep(0.5)
        try:
            for o in r['response']['items']:
                print (o['player'])  #[0]['url']   
                FLINK.write(f"{o['player']};{G['title']}\n")
        except KeyError:
            print (r)
            
    FLINK.close() 
get_a()
