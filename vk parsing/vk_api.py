# -*- coding: utf-8 -*-
import requests
import os, time, json
from datetime import datetime,  date

vk_id = "" # ID группы 

access_token = "" 


# Загрузка файлов
class DATA(object):
   def __init__(self):
       self.file = {}
   def parseIMG(self, dir_name):
       path = f"{dir_name}/"
       print ("PARSING",path)
       for r, d, f in os.walk(path):
           for ix, file in enumerate(f[:]): 
                      #print (r.split("/")[-1], os.path.join(r, file))
                      if ".jpg" in file.lower(): 
                          try:
                            self.file[r.split("/")[-1]].append(os.path.join(r, file))
                          except KeyError:
                            self.file[r.split("/")[-1]] = [os.path.join(r, file)]   
                            

#----------------------------------------------->  

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

def get_list_groups()
    # ПОЛУЧАЮ КАТАЛОГ ГРУПП
    URL = f"https://api.vk.com/method/groups.getCatalogInfo?&count=100&offset=200&access_token={access_token}&v=5.92"

    r = requests.get(url = URL) 
    data = r.json()
    data_0 = data['response']['categories'] 
    #print data_0
    for ix in data_0:
        print ix['id'], ix['name']

    # ЗАХОЖУ В КАТЕГОРИЮ 
    idx = 0
    for ix in data_0:
        URL = f"https://api.vk.com/method/groups.getCatalog?&category_id="+str(ix['id'])+"&count=100&offset=200&access_token={access_token}&v=5.92"
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
#----------------------------------------------->    

"""
Удалить данные с стены группы

"""
def del_data_wall(vk_id):
    s_offset = 0
    error = []
    G = True
    while G:
        URL = f"https://api.vk.com/method/wall.get?owner_id=-{vk_id}&count=100&offset={s_offset}&access_token={access_token}&v=5.92"
        r = requests.get(url = URL) 
        data = r.json() 
        if len(data['response']['items']) != 0:
            for ix, h in enumerate(data['response']['items']):
                try:
                    dt_object = datetime.fromtimestamp(h["date"]).strftime('%Y-%-m-%-d')
                    z = str(dt_object).split(" ")[0]
                    year, month, day = z.split("-")
                    date2 = date(int(year), int(month), int(day))
                    if date1>=date2:
                        URL1 = f"https://api.vk.com/method/wall.delete?owner_id=-{vk_id}&post_id={h['id']}&access_token={access_token}&v=5.92"
                        p = requests.get(URL1)
                        print (p.json(), date1>=date2, date1, date2, h['id'])
                        time.sleep(2)    
                    
                except KeyError:
                    pass
        else:
            G = False 
        s_offset += 100
        time.sleep(1)
        


#####################################
############# VIDEO #################
#####################################
"""
Добавить видео

"""
def add_videos_album(vk_id):
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


"""
Получить альбом и ссылки видео из группы, сохранить в файл

"""
def get_video_from_album(vk_id):
    URL = f"https://api.vk.com/method/video.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    FLINK = open(f"{vk_id}_video_link.txt","w")
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

"""
Удалить видео с альбомов 

"""
def del_videos_from_album(vk_id):

    URL = f"https://api.vk.com/method/video.get?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    for G in data['response']['items']:
        try:      
            URL1 = f"https://api.vk.com/method/video.removeFromAlbum?target_id=-{vk_id}&owner_id={G['owner_id']}&album_id={G['album_id']}&access_token={access_token}&v=5.92&video_id={G['id']}"
            r = requests.get(url = URL1).json() 
            print (r)
            #print (r, G['album_id'], URL1)
            time.sleep(0.5)
        except KeyError:
            print ("ERROR", G)  

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
    if len(data) != 0:    
        del_videos()

def _album_video(vk_id):
    URL = f"https://api.vk.com/method/video.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    print (data)
            

#####################################
############# IMAGES ################
#####################################

"""
Отправить изображение на стену группы/пользователя

"""
def post_to_wall(vk_id, file_name):
    message_text_utf = 'Загрузка картинки'
    message_text = message_text_utf.decode('utf-8')

    # Получаем ссылку для загрузки изображений
    method_url = 'https://api.vk.com/method/photos.getWallUploadServer?'
    data = dict(access_token=access_token, group_id=vk_id, v=5.92)
    response = requests.post(method_url, data)
    result = json.loads(response.text)
    print (result)
    upload_url = result['response']['upload_url']

    # Загружаем изображение на url
    response = requests.post(upload_url, files={'photo': open(file_name, 'rb')}).json()
    
    #params = {'server': response.json()['server'],
    #          'photo': response.json()['photo'],
    #          'hash': response.json()['hash'],
    #          'group_id': 47376425}
    
    # Сохраняем фото на сервере и получаем id
    method_url = 'https://api.vk.com/method/photos.saveWallPhoto?'
    data = dict(access_token=access_token, 
                group_id=vk_id, 
                photo=response['photo'], 
                hash=response['hash'], 
                server=response['server'], 
                v=5.92)
    response = requests.post(method_url, data).json()
    print (response)#['response'][0]['id'])

    # Теперь этот id остается лишь прикрепить в attachments метода wall.post
    # 'идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-"'
    method_url = 'https://api.vk.com/method/wall.post?'
    data = dict(access_token=access_token, owner_id=-47376425, attachments='photo'+ str(response.json()['response'][0]['owner_id'])+ '_'+ str(response.json()['response'][0]['id']), message=message_text, v=5.92)
    response = requests.post(method_url, data).json()
    print (response)


"""
Создать альбом и загрузить изображения из папки

"""
def create_album_from_dir_folder(vk_id):
    D = DATA()
    D.parseIMG("VK")
    for name in D.file:
        URL = f"https://api.vk.com/method/photos.createAlbum?group_id={vk_id}&access_token={access_token}&v=5.92&title={name}&upload_by_admins_only=1"
        r = requests.get(url = URL).json()
        print (name, r) 
        time.sleep(1) 
        
        id_album = r["response"]["id"]
        for _file in D.file[name]:
            method_url = 'https://api.vk.com/method/photos.getUploadServer?'
            data_to_vk = dict(access_token=access_token, group_id=vk_id, album_id=id_album, v=5.92)
            response = requests.post(method_url, data_to_vk).json()
            time.sleep(0.5) 
            print (response)
            upload_url = response['response']['upload_url'] 
            response = requests.post(upload_url, files={'photo': open(_file, 'rb')}).json()
            print (response)
            time.sleep(0.3) 
            
            
            
            method_url = 'https://api.vk.com/method/photos.save?'
            data = dict(access_token=access_token, 
                        group_id=vk_id, 
                        album_id=id_album,
                        photos_list=response['photos_list'], 
                        hash=response['hash'], 
                        server=response['server'], 
                        v=5.92)
            response = requests.post(method_url, data).json()
            print (response)              
            time.sleep(1)
        time.sleep(5)

"""
Получить изображения из альбома группы, сохранить на диск

"""
def get_image_album(vk_id)
    URL = f"https://api.vk.com/method/photos.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"
    r = requests.get(url = URL) 
    data = r.json() 
    #print (data)
    for G in data['response']['items']:
        os.mkdir(f"{vk_id}_VK/{G['title']}")
        URL_get = f"https://api.vk.com/method/photos.get?owner_id=-{vk_id}&album_id={G['id']}&access_token={access_token}&v=5.92"
        r = requests.get(url = URL_get).json() 
        for o in r['response']['items']:
            name_save = o['sizes'][-1]['url'].split("?")[0].split("/")[-1]
            namefl = o['sizes'][-1]['url']
            p = requests.get(namefl)
            out = open(f"{vk_id}_VK/{G['title']}/{name_save}", "wb")
            out.write(p.content)
            out.close() 
            time.sleep(0.5)
            
"""
Получить изображения с страници группы, сохранить на диск

"""
def get_image_wall(vk_id):
    error = []
    s_offset = 0
    count = 100
    G = True
    try:
        os.mkdir(vk_id)
    except Exception as e:
        print (e)
    
    while G:
        URL = f"https://api.vk.com/method/wall.get?owner_id=-{vk_id}&count={count}&offset={s_offset}&access_token={access_token}&v=5.92"
        r = requests.get(url = URL) 
        data = r.json() 
        if len(data['response']['items']) != 0:
            for ix, h in enumerate(data['response']['items']):
                try:
                    ZZZ = h['attachments']
                    for L in ZZZ:
                        namefl = L['photo']['sizes'][-1]['url']
                        p = requests.get(namefl)
                        namefl = namefl.split("?")[0].split("/")[-1]
                        out = open(f"{vk_id}/{h['id']}_{namefl}", "wb")
                        out.write(p.content)
                        out.close()
                        time.sleep(0.3) 

                    
                except KeyError:
                    error.append(h)
                    print (h, "\n")
        else:
            G = False 
        s_offset += count
        time.sleep(1)
        print (s_offset)
        
    with open(f"{vk_id}_wall_error.json", 'w') as js_file:
        json.dump(error, js_file)  

"""
Копировать альбомы из группы

"""
def copy_album_from_group(vk_id, vk_id2):
    URL = f"https://api.vk.com/method/photos.getAlbums?owner_id=-{vk_id}&access_token={access_token}&v=5.92"

    r = requests.get(url = URL) 
    data = r.json() 
    for G in data['response']['items']:
        print(G['title'])
        URL1 = f"https://api.vk.com/method/photos.createAlbum?group_id={vk_id2}&access_token={access_token}&v=5.92&title={G['title']}&upload_by_admins_only=1"
        r = requests.get(url = URL1).json() 
        print (r)

"""
Удалить все альбомы изображений группы

"""
def del_album(vk_id):
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



if __name__ == "__main__":
    print ("START API")
    #del_videos_from_album()

    #add_videos_album()

    #del_videos()

    #del_album() 
            
    #del_data_wall()

    #create_album_from_dir_folder()

