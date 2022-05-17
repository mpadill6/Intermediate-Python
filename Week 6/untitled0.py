# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:16:30 2020

@author: mpadilla
"""

class SingletonRestaurant(object):
    def __init__ (self,*args):
        print(f"Singleton Restaurant.__init__: (args)")
        
    def __new__(cls, *args, **kwargs):
        print (f"SingletonRestaurant.__new__: (args)")
        if not hasattr(cls,'_instance'):
            print(" Creating new instance ")
            cls._instance=super(SingletonRestaurant,cls).__new__(cls, *args, **kwargs)
        else:
            print(" Using existing instance ")
        return cls._instance
