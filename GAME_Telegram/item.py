import random
import time

items = [{"id":7, "name":"no wepon", "skill":8, "strength":0}, {"id":9, "name":"knuckles", "skill":8, "strength":35, }, {"id":5,"name":"Nonme"}]

class Item():
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
       
    def get_dict(self, x):
       for ix, g in enumerate(x):
           dict = self.__dict__.copy()
           for i in g.keys():
               dict[i] = g[i]
           x[ix] = dict    
           
if __name__ == "__main__":       
        it = Item()  
        get = it.get_dict(items)           
        print (items)
      



