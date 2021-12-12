import random
import time


#{"id":7, "name":"no wepon", "skill":8, "strength":0}
#items = [{"id":7, "name":"no wepon", "skill":8, "strength":0}, {"id":9, "name":"knuckles", "skill":8, "strength":35, }]

#class Item():
#    def __init__(self):
#    
#       self.id = 0
#       self.name = 0
#       self.skill = 0
#       #Характеристики оружия
#       
#       self.strength = 0 #Сила
#       self.health = 0 #Здоровье
#       self.speed = 0 #Скорость
#       self.agility = 0 #Ловкость
#       self.accuracy = 0 #Точность
#       self.courage = 0 #Смелость
#       self.demage = 0 #Урон
#       self.life = 0 #Жизнь
#       self.dodge = 0 #Уворот
#       self.antidodge = 0 #Антиуворот
#       self.criticalhit = 0 #Критический удар
#       self.anticriticalhit = 0 #Антикритический удар
#       self.weight = 0 # Вес
#       self.stamina = 0 #Прочность
#       self.breaking_through = 0 #Пробитие
#       
#    def get_dict(self, x):
#       for ix, g in enumerate(x):
#           dict = self.__dict__.copy()
#           for i in g.keys():
#               dict[i] = g[i]
#           x[ix] = dict    
#       
#it = Item()  
#get = it.get_dict(items)           
#print (items)
#      

#class User()
#    def __init__(self, name):

#class Fight()
#    def __init__(self): 

class Char():
    def __init__(self, name):
        self.name = name
        self.lvl = 0
        #Навык
        self.skill = 0
        #Предмет
        self.itm = 0
        #Характеристики
        self.hpp = 100 #Здоровье
        self.str = 0 #Сила
        self.agl = 0 #Ловкость
        self.acc = 0 #Точность
        self.brv = 0 #Смелость
        self.spd = 0 #Скорость
        #Навыки боя
        self.fgt = 0 # голые кулаки/рукопашный бой
        self.clb = 0 # Биты
        self.brs = 0 #Кастет
        self.knf= 0 #Нож
        #Навыки игры
        self.anatomy = 0 #Анатомия
        self.theft = 0 #Воровство
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
        
    
    def Hit(self):
        pass  
    def Dodge(self):
        pass
    def AntiDodge(self):
        pass   
    def CriticalHit(self):
        pass
    def AntiCriticalHit(self):
        pass
             
class Level():
    def __init__(self):
       self.lvl = 0
       self.point = 0
       self.all_point = 0             



