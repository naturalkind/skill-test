# -*- coding: utf-8 -*-
print "Hello I am bot"
"""
Коптер не забываю про коптер!!!

Сначала скачать все гуппы вк
Потом с каждой группы выбрать самые популярные посты
сранивать с лучшими из группы и выбирать 5-10
потом к-средних узнать среднюю оценку?
или выбрать лучшее из лучших
Обучить сеть и сравнивать по к средних цвета
что бы бот постил и выбирал самые лучшие посты

Что мне понадобиться
словарь a_dict = {} - ключ имя картинки, лайки просмотры
сохранять в папку с подпапками имени группы или ид



"""
import requests
#https://oauth.vk.com/authorize?client_id=XXXXXXX&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token 
#https://oauth.vk.com/blank.html#access_token=374c75d8fbce38d50b93b2d87a491fb330ae95f8a89a2a67acd09ffc2bb624e64699ceefc63279234b96c&expires_in=0&user_id=33923843&email=nerevaren@mail.ru
# ПРОБУЮ КАЧАТЬ
def get_photo(idx):
        URL = "https://api.vk.com/method/wall.get?owner_id=-"+idx+"&count=100&offset=200&access_token=374c75d8fbce38d50b93b2d87a491fb330ae95f8a89a2a67acd09ffc2bb624e64699ceefc63279234b96c&v=5.92"
        r = requests.get(url = URL) 
          
        data = r.json() 
        data2 = data['response']
        data3 = data2['items']
        for ix, h in enumerate(data3):
          try:
             namefl = h[u'attachments'][0]['photo']['sizes'][-1]['url']
             print "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", ix, type(h[u'attachments']), namefl.split('/')[-1]#h[u'attachments'][0]['photo']['sizes'][-1]['url']#.keys()#h.keys(), 
             p = requests.get(namefl)
             out = open("new/"+namefl.split('/')[-1], "wb")
             out.write(p.content)
             out.close()
          except KeyError:
             print "ERROR"




# ПОЛУЧАЮ КАТАЛОГ ГРУПП
URL = "https://api.vk.com/method/groups.getCatalogInfo?&count=100&offset=200&access_token=374c75d8fbce38d50b93b2d87a491fb330ae95f8a89a2a67acd09ffc2bb624e64699ceefc63279234b96c&v=5.92"

r = requests.get(url = URL) 
data = r.json()
data_0 = data['response']['categories'] 
#print data_0
for ix in data_0:
    print ix['id'], ix['name']

# ЗАХОЖУ В КАТЕГОРИЮ 
idx = 0
for ix in data_0:
    URL = "https://api.vk.com/method/groups.getCatalog?&category_id="+str(ix['id'])+"&count=100&offset=200&access_token=374c75d8fbce38d50b93b2d87a491fb330ae95f8a89a2a67acd09ffc2bb624e64699ceefc63279234b96c&v=5.92"
    r = requests.get(url = URL)
    data = r.json()
    
    try:
            data = data['response']['items']
            #print data
            for ixx in data:
                print ixx['id'], ixx['screen_name'], ixx['is_closed'], ixx['name']
                get_photo(str(ixx['id']))
                idx += 1
    except:
            print "ERRORRRs", data

print idx



