import random
import time

class Char():
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
    #def calculate_damage(self, damage_amount, attacker):    
    #plr(1, 14) = rTab.Range("base_dmg").Cells.Value + ((plr(1, 1) + item(1, 4)) * rTab.Cells(7, 5).Value) + ((plr(1, 2) + item(1, 5)) * rTab.Cells(8, 5).Value) + ((plr(1, 3) + item(1, 6)) * rTab.Cells(9, 5).Value) + ((plr(1, 4) + item(1, 7)) * rTab.Cells(10, 5).Value) + ((plr(1, 5) + item(1, 8)) * rTab.Cells(11, 5).Value) + ((plr(1, 6) + item(1, 9)) * rTab.Cells(12, 5).Value) + (plr(1, 8) * rTab.Cells(13, 5).Value) + (plr(1, 9) * rTab.Cells(14, 5).Value) + (plr(1, 10) * rTab.Cells(15, 5).Value) + (plr(1, 11) * rTab.Cells(16, 5).Value) + (plr(1, 12) * rTab.Cells(17, 5).Value) + (plr(1, 13) * rTab.Cells(18, 5).Value) + item(1, 10)
    # Базовый урон это 5 столбик, rTab.Range("base_dmg") = 1
    # 5+3
    
    #COF_DMG_str = 3 #char.сила!
    #COF_DMG_spd = 0 #char.скорость!
    #COF_DMG_agl = 0.48 #char.скорость!
    #COF_DMG_acc = 0.88 #char.меткость!
    #COF_DMG_brv = 0 # char.смелость!
    #COF_DMG_hpp = 0 # char.здоровье!
    #dmg
    #plr(1, 14) = 1 + ((char.сила + item.сила) * char.сила!) + 
    #              ((char.здоровье + item.здоровье) * char.здоровье!) + 
    #              ((char.скорость + item.скорость) * char.скорость!) + 
    #              ((char.ловкость + item.ловкость) * char.ловкость!) + 
    #              ((char.меткость + item.меткость) * char.меткость!) + 
    #              ((char.смелость + item.смелость) * char.смелость!) + 
    #              (char.рукопашный * char.рукопашный!) + 
    #              (char.биты * char.битыe!) + 
    #              (char.кастеты * char.кастеты!) + 
    #              (char.ножи * char.ножи!) + 
    #              (char.анатомия * char.анатомия!) + 
    #              (char.воровство * char.воровство!) + 
    #              item.урон   
        #self.dmg = (self.str+)*-
    # Global **!  
    

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
Player1.str = 30  


#Player 2
Player2 = Char()    
Player2.agl = 30 

print (Player1.__dict__, Player2.__dict__)

