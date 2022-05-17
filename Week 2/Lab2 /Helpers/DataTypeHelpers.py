# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:37:36 2020

@author: mpadilla
"""
__all__= ["isInt", "isFloat", "isDate"]

    

        
def isInt(integer):
       value_sign=integer.lstrip("+-")
       if value_sign.isnumeric()==True:
            return True
       else:
            return False
def isFloat(flt):
        try:
            num=float(flt)
            return True
        except:
            return False
def isDate(date_input):
        try:
            date=date_input.split("-")
            if int(date[0]) > 0 and int(date[1])>0 and int(date[1])<13 and int(date[2])>0 and int(date[2])<32:
                return True             
        except:
               return False




