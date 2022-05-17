# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:16:30 2020

@author: mpadilla
"""
from time import sleep

class SingletonRestaurant(object):
    _orders=0
    _total_sales=0
    # def __init__ (self,*args):
    #     print(f"Singleton Restaurant.__init__: {args}")
               
    def __new__(cls, *args, **kwargs):
        print (f"{SingletonRestaurant.__new__}: (args)")
        if not hasattr(cls,'_instance'):
            print(" Creating new instance ")
            cls._instance=super(SingletonRestaurant,cls).__new__(cls, *args, **kwargs)

        else:
            print(" Using existing instance ")
        return cls._instance
    def __str__(self):
        return f"The total number of orders for the day are {self._orders} "
  
    def order_food(self,food_type):
         Food.order_food(food_type)
         self._orders+=1
class Food():
    def __init__(self):
        print("Starting Order")
    
    def price(self):
        return 0
    
    def prepare(self,food_type):
        if food_type.lower() =='pasta':
            Pasta.prepare()
        if food_type.lower() =='cheeseburger':
            Cheeseburger.prepare()
        if food_type.lower() =='steak':
            obj_steak=Steak()
            obj_steak.prepare()           
    
    @staticmethod
    def order_food(food_type):
        if food_type.lower() =='pasta':
            obj_pasta=Pasta()
            obj_pasta.prepare()
        if food_type.lower() =='cheeseburger':
            obj_cheeseburger=Cheeseburger()
            obj_cheeseburger.prepare()
        if food_type.lower() =='steak':
            obj_steak=Steak()
            obj_steak.prepare()
        

class Cheeseburger(Food):
    
    def __str__(self):
        return f"{__class__.__name__}: { self.price()}"
    
    
    def price(self):
        return 5.99
    
    def prepare(self):
        print (f"{__class__.__name__}: grill all beef patty")
        sleep(2)
        print (f"{__class__.__name__}: flip all beef patty")
        sleep(2)
        print (f"{__class__.__name__}: put cheese on all beef patty")
        sleep(2)
        print (f"{__class__.__name__}: put all beef patty on bun and add toppings")
        sleep(2)
        print (f"{__class__.__name__}: All Done!")
        sleep(2)
        print (f"{__class__.__name__}: {self.price()}")
  
class Steak(Food):
    
    def __str__(self):
        return f"{__class__.__name__}: {self.price()}"
    
    
    def price(self):
        return 19.99
    
    def prepare(self):
        print (f"{__class__.__name__}: sautee the garlic and herbs")
        sleep(2)
        print (f"{__class__.__name__}: place potato in oven")
        sleep(2)
        print (f"{__class__.__name__}: melt butter")
        sleep(2)
        print (f"{__class__.__name__}: put steak on pan")
        sleep(2)
        print (f"{__class__.__name__}: flip steak over")
        sleep(2)
        print (f"{__class__.__name__}: plate steak and place roasted potato on side")
        sleep(2)
        print (f"{__class__.__name__}: All Done!")
        sleep(2)
        print (f"{__class__.__name__}: {self.price()}")  


class Pasta(Food):
    
    def __str__(self):
        return f"{__class__.__name__}: {self.price()}"
    
    
    def price(self):
        return 9.99
    
    def prepare(self):
        print (f"{__class__.__name__}: boil water for noodles")
        sleep(2)
        print (f"{__class__.__name__}: saute onions, garlic and tomatoes")
        sleep(2)
        print (f"{__class__.__name__}: put noodles in water")
        sleep(2)
        print (f"{__class__.__name__}: season the sauce")
        sleep(2)
        print (f"{__class__.__name__}: plate noodles and add sauce on top")
        sleep(2)
        print (f"{__class__.__name__}: All Done!")
        sleep(2)
        print (f"{__class__.__name__}: {self.price()}") 
        
def main():
    r=SingletonRestaurant()
    food=r.order_food("pasta")
    food=r.order_food("cheeseburger")
    food=r.order_food("steak")
    print(r)
        
 #Use this test to prove we have a single instance of SingletonRestaurant   
    r2=SingletonRestaurant()
    print(r2)

if __name__=='__main__':
    main()


