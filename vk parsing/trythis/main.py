# -*- coding: utf-8 -*-
import os
import config
#import urllib
#import urllib2
import requests
import json

token = '261beb8cbe14581fd4c8edf0805d505a05d439816bc27beedd9051b75ce84e768a100d149727811aeb5a8'#config.vk_token

def post():
        #url='http://trolleway.nextgis.com/api/component/render/image?resource=642&extent=-9273652.2898957,5017436.116284987,-9273230.09474728,5017965.801004432&size=708,888'
        message_text_utf='Загрузка картинки'
        message_text = message_text_utf.decode('utf-8')

        # Получаем ссылку для загрузки изображений
        method_url = 'https://api.vk.com/method/photos.getWallUploadServer?'
        #data = dict(access_token=token, owner_id=-47376425, v=5.92)
        data = dict(access_token=token, group_id=47376425, v=5.92)
        response = requests.post(method_url, data)
        result = json.loads(response.text)
        print result
        upload_url = result['response']['upload_url']

        # Загружаем изображение на url
        response = requests.post(upload_url, files={'photo': open("a3ehsSOKMUY.jpg", 'rb')})
        #result = json.loads(response.text)
        
        #params = {'server': response.json()['server'],
        #          'photo': response.json()['photo'],
        #          'hash': response.json()['hash'],
        #          'group_id': 47376425}
        print "DDDD",response, response.json()['server']
        # Сохраняем фото на сервере и получаем id
        method_url = 'https://api.vk.com/method/photos.saveWallPhoto?'
        #data = dict(access_token=token, owner_id=-47376425, photo=result['photo'], hash=result['hash'], server=result['server'])
        data = dict(access_token=token, group_id=47376425, photo=response.json()['photo'], hash=response.json()['hash'], server=response.json()['server'], v=5.92)
        response = requests.post(method_url, data)
        print response.json()#['response'][0]['id']
        #result = json.loads(response.text)['response'][0]['id']

        # Теперь этот id остается лишь прикрепить в attachments метода wall.post
        # 'идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-"'
        method_url = 'https://api.vk.com/method/wall.post?'
        data = dict(access_token=token, owner_id=-47376425, attachments='photo'+ str(response.json()['response'][0]['owner_id'])+ '_'+ str(response.json()['response'][0]['id']), message=message_text, v=5.92)
        response = requests.post(method_url, data)
        #result = json.loads(response.text)
        print response.json()

post()
