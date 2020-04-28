# -*- coding: utf-8 -*-

BT_S = {"inline_keyboard": [[dict(text = "Голова", callback_data = "/hithead"),
                           dict(text = "Голова", callback_data = "/blockhead")],
                          [dict(text = "Грудь", callback_data = "/hitchest"),
                           dict(text = "Грудь", callback_data = "/blockchest")],
                          [dict(text = "Живот", callback_data = "/hitbelly"),
                           dict(text = "Живот", callback_data = "/blockbelly")],
                          [dict(text = "Ноги", callback_data = "/hitlegs"),
                           dict(text = "Ноги", callback_data = "/blocklegs")],
                          [dict(text = "↑ Удары 🤜 2", callback_data = "/hit_count"),
                           dict(text = "❤ 100 ☑ 3", callback_data = "/health"),
                           dict(text = "2 🙌 Блоки ↑", callback_data = "/block_count")],
                          [dict(text = "СТАРТ", callback_data = "/hit")]
                          ]} 
                          
BT = {"inline_keyboard": [
                                [{
                                    "text": "ardor.minbashi.com",
                                    "url":"http://ardor.minbashi.com/"
                                }],
                                [{
                                    "text": "Продолжить, мне 18",
                                    "callback_data": "/age"
                                }],
                                [{
                                    "text": "Изменить на EN",
                                    "callback_data": "/A1"
                                }],
                                [{
                                    "text": "◀ ", #\xE2\x97\x80
                                    "callback_data": "/left"
                                },
                                {
                                    "text": "💬", #\xF0\x9F\x92\xAC /🗨
                                    "callback_data": "/lang"            
                                },
                                {
                                    "text": " ▶", #\xE2\x96\xB6
                                    "callback_data": "/right"            
                                }],
                                [{
                                    "text": "Покинуть игру",
                                    "callback_data": "/endgame"                                   
                                }]
                                ]}                           
                            
#TEST = "/hitbelly"                                
def get_BTS(TEST):
    
#    if BT_S["inline_keyboard"][-1][0]:
#       
#    if BT_S["inline_keyboard"][-1][1]:
    for z in BT_S["inline_keyboard"][:-2]:
        if z[0]['callback_data'] == TEST:
           z[0]["text"] += " 🤜"
           print (z)
        if z[1]['callback_data'] == TEST:   
           z[1]["text"] = "🙌 " + z[1]["text"]
    #return BT_S      
           
#print (BT_S)    
       
#listHIT = {"/blockchest":"🙌 Грудь", "/blockbelly":"🙌 Живот", "/blocklegs":"🙌 Ноги", "/blockhead":"🙌 Голова", 
#           "/hitbelly":"Живот 🤜", "/hitlegs":"Ноги 🤜", "/hithead":"Голова 🤜" , "/hitchest":"Грудь 🤜"}
