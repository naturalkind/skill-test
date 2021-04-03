# -*- coding: utf-8 -*-
import requests
import os, time
access_token = "261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8"


def del_album():
    vk_id = "67267231"  #skynet
    #vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/photos.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    print (data)
    for G in data['response']['items']:
        if G['title'] != "СХЕМЫ":
            #print(G['title'], G['id'])
            URL1 = f"https://api.vk.com/method/photos.deleteAlbum?group_id={vk_id}&access_token={access_token}&v=5.92&album_id={G['id']}"
            r = requests.get(url = URL1).json() 
            print (r)
            time.sleep(0.5)


def del_album_video():
    vk_id = "67267231" # skynet
    #vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/video.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    print (data)
#    for G in data['response']['items']:
#        if G['title'] != "СХЕМЫ":
#            #print(G['title'], G['id'])
#            URL1 = f"https://api.vk.com/method/photos.deleteAlbum?group_id={vk_id}&access_token={access_token}&v=5.92&album_id={G['id']}"
#            r = requests.get(url = URL1).json() 
#            print (r)
#            time.sleep(0.5)

def del_videos():
    vk_id = "67267231" # skynet
    #vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/video.get?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    print (data)
    for G in data['response']['items']:
        print (G["id"])        
        URL1 = f"https://api.vk.com/method/video.delete?access_token={access_token}&v=5.92&video_id={G['id']}&target_id=-{vk_id}&owner_id={G['owner_id']}"
        r = requests.get(url = URL1).json() 
        print (r)
        time.sleep(0.5)

def del_videos_from_album():
    vk_id = "67267231" # skynet
    #vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/video.get?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    for G in data['response']['items']:
        #print (G)
        
        try:      
            URL1 = f"https://api.vk.com/method/video.removeFromAlbum?target_id=-{vk_id}&owner_id={G['owner_id']}&album_id={G['album_id']}&access_token={access_token}&v=5.92&video_id={G['id']}"
            r = requests.get(url = URL1).json() 
            print (r, "-------------------->")
            #print (r, G['album_id'], URL1)
            time.sleep(0.5)
        except KeyError:
            print (G)  
            
            
def add_videos_album():
    vk_id = "67267231" # skynet
    #vk_id = "47376425" #цифровая копия
    URL = f"https://api.vk.com/method/video.get?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    for G in data['response']['items']:
        #print (G)
        
        try:      
            URL1 = f"https://api.vk.com/method/video.addToAlbum?target_id=-{vk_id}&owner_id={G['owner_id']}&album_id=1&access_token={access_token}&v=5.92&video_id={G['id']}"
            r = requests.get(url = URL1).json() 
            print (r,"-------------------->")
            #print (r, G['album_id'], URL1)
            time.sleep(0.5)
        except KeyError:
            print (G)            

#del_videos_from_album()

#add_videos_album()

del_videos()
