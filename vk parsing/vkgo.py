# -*- coding: utf-8 -*-

#код доступа
#bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009

#https://api.vk.com/method/users.get?
#user_ids=210700286&fields=bdate&
#access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92

import requests

#URL = "https://api.vk.com/method/users.get?user_ids=33923843&fields=bdate&access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92"
#URL = "https://api.vk.com/method/wall.get?owner_id=-3754163&count=100&offset=200&access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92"
vk_id = "-47376425"
vk_id = "-101748595"
URL = "https://api.vk.com/method/wall.get?owner_id="+ vk_id +"&count=100&offset=200&access_token=bbadc56bbbadc56bbb1f5be876bbf7d89dbbbadbbadc56be314036c5110736080a91009&v=5.92"
#offset=200 - смещение
#47376425 group ??
#87891112 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
data2 = data['response']
data3 = data2['items']
#print data2['items'], len(data3)#.keys()
for ix, h in enumerate(data3):
  try:
     namefl = h[u'attachments'][0]['photo']['sizes'][-1]['url']
     print ("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", ix, type(h[u'attachments']), namefl.split('/')[-1])#h[u'attachments'][0]['photo']['sizes'][-1]['url']#.keys()#h.keys(), 
     p = requests.get(namefl)
     out = open("foto2/"+namefl.split('/')[-1], "wb")
     out.write(p.content)
     out.close()
  except KeyError:
     print ()# h.keys()

"""
p = requests.get(img)
out = open("...\img.jpg", "wb")
out.write(p.content)
out.close()
"""

