import random
import time

class Modificator():
    def __init__(self):
        self.base_dmg = 1
        self.base_ddg = 0
        self.base_adg = 0
        self.base_crt = 0
        self.base_lfe = 20
        self.base_act = 0
        
    def cof_dmg(self):
            return dict( cof_str = 3, #char.сила!
                         cof_hpp = 0, # char.здоровье! 
                         cof_spd = 0, #char.скорость!
                         cof_agl = 0.48, #char.скорость!
                         cof_acc = 0.88, #char.меткость!
                         cof_brv = 0) # char.смелость!
                         
    def cof_ddg(self):
            return dict( cof_str = 0, #char.сила!
                         cof_hpp = 0, # char.здоровье! 
                         cof_spd = 0, #char.скорость!
                         cof_agl = 0, #char.скорость!
                         cof_acc = 1.6, #char.меткость!
                         cof_brv = 0) # char.смелость!
                         
    def cof_lfe(self):
            return dict( cof_str = 0, #char.сила!
                         cof_hpp = 5, # char.здоровье!       
                         cof_spd = 0, #char.скорость!
                         cof_agl = 0, #char.скорость!
                         cof_acc = 0, #char.меткость!
                         cof_brv = 0) # char.смелость!
                                           

if __name__ == "__main__":              
        M = Modificator()
        print (M.__dict__)
        print (M.cof_dmg(), M.cof_ddg())
        
        
# Очистка сообщений
# Кнопки:
#  передача данных, кнопка перехода на url
#  передача номера телефоноа
#  передача геолокации       
# Уметь выводить информацию в активные сообщения не удаляем а обновляем (edit)
# Выводить инфомации в несколько активных сообщений
# Ограничения по количество сообщений

