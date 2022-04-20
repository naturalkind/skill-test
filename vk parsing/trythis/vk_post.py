# -*- coding: utf-8 -*-

#https://api.vk.com/method/users.get?
#user_ids=210700286&fields=bdate&

import requests
access_token = "261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8"

#URL = f"https://api.vk.com/method/users.get?user_ids=33923843&fields=bdate&access_token={access_token}&v=5.92"
URL = f"https://api.vk.com/method/wall.post?owner_id=-47376425&message=HELLO&access_token={access_token}&v=5.92"
r = requests.get(url = URL) 
#https://oauth.vk.com/blank.html#access_token=261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8&expires_in=0&user_id=33923843&email=nerevaren@mail.ru #token
#https://oauth.vk.com/authorize?client_id=5905910&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,messages,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token 
data = r.json() 
print data


