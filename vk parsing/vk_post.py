# -*- coding: utf-8 -*-

#код доступа
#bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009

#https://api.vk.com/method/users.get?
#user_ids=210700286&fields=bdate&
#access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92

import requests

#URL = "https://api.vk.com/method/users.get?user_ids=33923843&fields=bdate&access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92"
URL = "https://api.vk.com/method/wall.post?owner_id=-47376425&message=HELLO&access_token=261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8&v=5.92"
#offset=200 - смещение
#47376425 group ?? 
#87891112 
#обучение с подкреплением
r = requests.get(url = URL) 
#https://oauth.vk.com/blank.html#access_token=261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8&expires_in=0&user_id=33923843&email=nerevaren@mail.ru #token
#https://oauth.vk.com/authorize?client_id=5905910&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,messages,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token 
data = r.json() 
print data



"""
mport os
import vk
from configs import login, password
import sys
import requests
import json
 
session = vk.AuthSession(app_id='6697996', user_login=login, user_password=password, scope='wall, messages, photos')
vk_api = vk.API(session, v='5.85')
groupID = '172368096'
 
upload_url = vk_api.photos.getWallUploadServer(group_id=groupID)['upload_url']
 
 
request = requests.post(upload_url, files={'photo': open('fer.jpg', "rb")})
params = {'server': request.json()['server'],
          'photo': request.json()['photo'],
          'hash': request.json()['hash'],
          'group_id': groupID}
 
 
data = vk_api.photos.saveWallPhoto(**params)
 
photo_id = data [0]['id']
 
params = {'attachments': 'photo'+ str(data [0]['owner_id']) + '_'+ str(photo_id),
          'message': 'test',
          'owner_id': '-' + groupID,
          'from_group': '1'}
vk_api.wall.post(**params)
"""
