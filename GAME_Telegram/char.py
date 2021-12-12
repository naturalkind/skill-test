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
    def calculate_damage(self, damage_amount, attacker):    
    #plr(1, 14) = rTab.Range("base_dmg").Cells.Value + 
    #            ((plr(1, 1) + item(1, 4)) * rTab.Cells(7, 5).Value) + 
    #            ((plr(1, 2) + item(1, 5)) * rTab.Cells(8, 5).Value) + 
    #            ((plr(1, 3) + item(1, 6)) * rTab.Cells(9, 5).Value) + 
    #            ((plr(1, 4) + item(1, 7)) * rTab.Cells(10, 5).Value) + 
    #            ((plr(1, 5) + item(1, 8)) * rTab.Cells(11, 5).Value) + 
    #            ((plr(1, 6) + item(1, 9)) * rTab.Cells(12, 5).Value) + 
    #            (plr(1, 8) * rTab.Cells(13, 5).Value) + 
    #            (plr(1, 9) * rTab.Cells(14, 5).Value) + 
    #            (plr(1, 10) * rTab.Cells(15, 5).Value) + 
    #            (plr(1, 11) * rTab.Cells(16, 5).Value) + 
    #            (plr(1, 12) * rTab.Cells(17, 5).Value) + 
    #            (plr(1, 13) * rTab.Cells(18, 5).Value) + item(1, 10)
    # Базовый урон это 5 столбик, rTab.Range("base_dmg") = 1
    # Урон = Базовый урон + Множитель таланта Базовый урон
    
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
    
    #Минимальный урон
    #Vars(4) = dam_dist = 0.3
    
    #plr(1, 15) = plr(1, 14) - (plr(1, 14) * Vars(4))

    #Максимальный урон
    #plr(1, 16) = plr(1, 14) + (plr(1, 14) * Vars(4))
    
    #Жизнь
    #plr(1, 17) = rTab.Range("base_lfe").Cells.Value + 
    #             ((char.сила + item(1, 4)) * rTab.Cells(7, 15).Value) + 
    #             ((char.здоровье + item(1, 5)) * rTab.Cells(8, 15).Value) + 
    #             ((char.скорость + item(1, 6)) * rTab.Cells(9, 15).Value) + 
    #             ((char.ловкость + item(1, 7)) * rTab.Cells(10, 15).Value) + 
    #             ((char.меткость + item(1, 8)) * rTab.Cells(11, 15).Value) + 
    #             ((char.смелость + item(1, 9)) * rTab.Cells(12, 15).Value) + 
    #             (char.рукопашный * rTab.Cells(13, 15).Value) + 
    #             (char.биты * rTab.Cells(14, 15).Value) + 
    #             (char.кастеты * rTab.Cells(15, 15).Value) + 
    #             (char.ножи * rTab.Cells(16, 15).Value) + 
    #             (char.анатомия * rTab.Cells(17, 15).Value) + 
    #             (char.воровство * rTab.Cells(18, 15).Value) + 
    #             item(1, 11)
    
    #Уворот
    #plr(1, 18) = rTab.Range("base_ddg").Cells.Value + 
    #             ((char.сила + item(1, 4)) * rTab.Cells(7, 7).Value) + 
    #             ((char.здоровье + item(1, 5)) * rTab.Cells(8, 7).Value) + 
    #             ((char.скорость + item(1, 6)) * rTab.Cells(9, 7).Value) + 
    #             ((char.ловкость + item(1, 7)) * rTab.Cells(10, 7).Value) + 
    #             ((char.меткость + item(1, 8)) * rTab.Cells(11, 7).Value) + 
    #             ((char.смелость + item(1, 9)) * rTab.Cells(12, 7).Value) + 
    #             (char.рукопашный * rTab.Cells(13, 7).Value) + 
    #             (char.биты * rTab.Cells(14, 7).Value) + 
    #             (char.кастеты * rTab.Cells(15, 7).Value) + 
    #             (char.ножи * rTab.Cells(16, 7).Value) + 
    #             (char.анатомия * rTab.Cells(17, 7).Value) + 
    #             (char.воровство * rTab.Cells(18, 7).Value) + 
    #             item(1, 12)
     
    #Антиуворот
    #plr(1, 19) = rTab.Range("base_adg").Cells.Value + 
    #             ((char.сила + item(1, 4)) * rTab.Cells(7, 9).Value) + 
    #             ((char.здоровье + item(1, 5)) * rTab.Cells(8, 9).Value) + 
    #             ((char.скорость + item(1, 6)) * rTab.Cells(9, 9).Value) + 
    #             ((char.ловкость + item(1, 7)) * rTab.Cells(10, 9).Value) + 
    #             ((char.меткость + item(1, 8)) * rTab.Cells(11, 9).Value) + 
    #             ((char.смелость + item(1, 9)) * rTab.Cells(12, 9).Value) + 
    #             (char.рукопашный * rTab.Cells(13, 9).Value) + 
    #             (char.биты * rTab.Cells(14, 9).Value) + 
    #             (char.кастеты * rTab.Cells(15, 9).Value) + 
    #             (char.ножи * rTab.Cells(16, 9).Value) + 
    #             (char.анатомия * rTab.Cells(17, 9).Value) + 
    #             (char.воровство * rTab.Cells(18, 9).Value) + 
    #             item(1, 13) 
      
    #Критическая атака
    #plr(1, 20) = rTab.Range("base_crt").Cells.Value + 
    #             ((char.сила + item(1, 4)) * rTab.Cells(7, 11).Value) + 
    #             ((char.здоровье + item(1, 5)) * rTab.Cells(8, 11).Value) + 
    #             ((char.скорость + item(1, 6)) * rTab.Cells(9, 11).Value) + 
    #             ((char.ловкость + item(1, 7)) * rTab.Cells(10, 11).Value) + 
    #             ((char.меткость + item(1, 8)) * rTab.Cells(11, 11).Value) + 
    #             ((char.смелость + item(1, 9)) * rTab.Cells(12, 11).Value) + 
    #             (char.рукопашный * rTab.Cells(13, 11).Value) + 
    #             (char.биты * rTab.Cells(14, 11).Value) + 
    #             (char.кастеты * rTab.Cells(15, 11).Value) + 
    #             (char.ножи * rTab.Cells(16, 11).Value) + 
    #             (char.анатомия * rTab.Cells(17, 11).Value) + 
    #             (char.воровство * rTab.Cells(18, 11).Value) + 
    #             item(1, 14)  
    
    #Антикрит
    #plr(1, 21) = rTab.Range("base_ctr").Cells.Value + 
    #             ((char.сила + item(1, 4)) * rTab.Cells(7, 13).Value) + 
    #             ((char.здоровье - plr(1, 1) + item(1, 5)) * rTab.Cells(8, 13).Value) + 
    #             ((char.скорость + item(1, 6)) * rTab.Cells(9, 13).Value) + 
    #             ((char.ловкость + item(1, 7)) * rTab.Cells(10, 13).Value) + 
    #             ((char.меткость + item(1, 8)) * rTab.Cells(11, 13).Value) + 
    #             ((char.смелость + item(1, 9)) * rTab.Cells(12, 13).Value) + 
    #             (char.рукопашный * rTab.Cells(13, 13).Value) + 
    #             (char.биты * rTab.Cells(14, 13).Value) + 
    #             (char.кастеты * rTab.Cells(15, 13).Value) + 
    #             (char.ножи * rTab.Cells(16, 13).Value) + 
    #             (char.анатомия * rTab.Cells(17, 13).Value) + 
    #             (char.воровство * rTab.Cells(18, 13).Value) + 
    #             item(1, 15)
      
    #Приемы
    #plr(1, 23) = ((char.сила + item(1, 4)) * rTab.Cells(7, 17).Value) + 
    #             ((char.здоровье + item(1, 5)) * rTab.Cells(8, 17).Value) + 
    #             ((char.скорость + item(1, 6)) * rTab.Cells(9, 17).Value) + 
    #             ((char.ловкость + item(1, 7)) * rTab.Cells(10, 17).Value) + 
    #             ((char.меткость + item(1, 8)) * rTab.Cells(11, 17).Value) + 
    #             ((char.смелость + item(1, 9)) * rTab.Cells(12, 17).Value) + 
    #             (char.рукопашный * rTab.Cells(13, 17).Value) + 
    #             (char.биты * rTab.Cells(14, 17).Value) + 
    #             (char.кастеты * rTab.Cells(15, 17).Value) + 
    #             (char.ножи * rTab.Cells(16, 17).Value) + 
    #             (char.анатомия * rTab.Cells(17, 17).Value) + 
    #             (char.воровство * rTab.Cells(18, 17).Value) - 
    #             item(1, 16)

    #plr(1, 22) = rTab.Range("base_act").Cells.Value + Int(plr(1, 23) / 1  
    #---------------------------------------------------------_>
    
    def calculate_heals(self, heal_amount):
        pass        
    
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

