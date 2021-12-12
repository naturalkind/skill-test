import random
import time


class Char():
    def __init__(self, name):
        self.name = name
        self.level = 0
        #Навык
        self.skill = 0
        #Характеристики
        self.health = 100 #Здоровье
        self.strength = 0 #Сила
        self.agility = 0 #Ловкость
        self.accuracy = 0 #Точность
        self.courage = 0 #Смелость
        self.speed = 0 #Скорость
        #Навыки боя
        self.hand2hand = 0 # голые кулаки
        self.bat = 0 # Биты
        self.knuckles = 0 #Кастет
        self.knife = 0 #Нож
        #Навыки игры
        self.anatomy = 0 #Анатомия
        self.theft = 0 #Воровство
        
    
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
             
class Level()
    def __init__(self):
       self.lvl = 0
       self.point = 0
       self.all_point = 0             

class Item()
    def __init__(self):
       self.id = 0
       self.name = 0
       self.skill = 0
       #Характеристики оружия
       
       self.strength = 0 #Сила
       self.health = 0 #Здоровье
       self.speed = 0 #Скорость
       self.agility = 0 #Ловкость
       self.accuracy = 0 #Точность
       self.courage = 0 #Смелость
       self.demage = 0 #Урон
       self.life = 0 #Жизнь
       self.dodge = 0 #Уворот
       self.antidodge = 0 #Антиуворот
       self.criticalhit = 0 #Критический удар
       self.anticriticalhit = 0 #Антикритический удар
       self.weight = 0 # Вес
       self.stamina = 0 #Прочность
       self.breaking_through = 0 #Пробитие

