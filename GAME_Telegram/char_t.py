import random
import time

class Char():
    COF_DMG_str = 3 #char.сила!
    COF_DMG_spd = 0 #char.скорость!
    COF_DMG_agl = 0.48 #char.ловкость!
    COF_DMG_acc = 0.88 #char.меткость!
    COF_DMG_brv = 0 # char.смелость!
    COF_DMG_hpp = 0 # char.здоровье!
    def __init__(self):
        self.name = 0
        self.lvl = 0
        #Навык
        self.skill = 0
        #Предмет
        self.itm = 0
        #-------------------------->
        #Характеристики
        #Настраевымые основные
        self.hpp = 0 #Здоровье 
        self.str = 0 #Сила
        self.agl = 0 #Ловкость
        self.acc = 0 #Точность
        #Настраевымые не основные
        self.brv = 0 #Смелость
        self.spd = 0 #Скорость
        #-------------------------->
        #Навыки боя
        #Настраевымые
        self.fgt = 0 # голые кулаки/рукопашный бой
        self.clb = 0 # Биты
        self.brs = 0 #Кастет
        self.knf= 0 #Нож
        #Навыки игры
        #Настраевымые
        self.anatomy = 0 #Анатомия
        self.theft = 0 #Воровство
        #-------------------------->
        #Рассчитываем на основе данных
        #Урон
        self.dmg = 0
        self.min_dmg = 0
        self.max_dmg = 0
        #Жизнь
        self.lfe = 0
        #Шанс
        self.ddg = 0 #Шанс уворота
        self.adg = 0 #Антиуворот
        self.crt = 0 #Критический
        self.ctr = 0 #Антикрит
        self.act = 0 #Прием
    def calculate_stat(self):    
        self.dmg = 1 + ((self.str + 0) * self.COF_DMG_str) + \
                  ((self.hpp + 0) * self.COF_DMG_hpp) + \
                  ((self.spd + 0) * self.COF_DMG_spd) + \
                  ((self.agl + 0) * self.COF_DMG_agl) + \
                  ((self.acc + 0) * self.COF_DMG_acc) + \
                  ((self.brv + 0) * self.COF_DMG_brv) + \
                  (self.fgt * 0) + \
                  (self.clb * 0) + \
                  (self.brs * 0) + \
                  (self.knf * 0) + (self.anatomy * 0) + \
                  (self.theft * 0) + 0
        self.min_dmg = self.dmg - (self.dmg * 0.3)
        
        self.max_dmg = self.dmg + (self.dmg * 0.3)
        
        
        self.dmg = 1 + ((self.str + 0) * self.COF_DMG_str) + \
                  ((self.hpp + 0) * 5) + \
                  ((self.spd + 0) * self.COF_DMG_spd) + \
                  ((self.agl + 0) * self.COF_DMG_agl) + \
                  ((self.acc + 0) * self.COF_DMG_acc) + \
                  ((self.brv + 0) * self.COF_DMG_brv) + \
                  (self.fgt * 0) + \
                  (self.clb * 0) + \
                  (self.brs * 0) + \
                  (self.knf * 0) + (self.anatomy * 0) + \
                  (self.theft * 0) + 0

#    def calculate_heals(self, heal_amount):
#        pass        
#    def Hit(self):
#        pass  
#    def Dodge(self):
#        pass
#    def AntiDodge(self):
#        pass   
#    def CriticalHit(self):
#        pass
#    def AntiCriticalHit(self):
#        pass

#Player 1             
Player1 = Char()
Player1.str = 49  
Player1.calculate_stat()
print (Player1.__dict__)

##Player 2
#Player2 = Char()    
#Player2.agl = 30 

#print (Player1.__dict__, Player2.__dict__)

