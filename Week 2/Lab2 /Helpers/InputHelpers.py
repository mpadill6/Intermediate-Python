# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:47:21 2020

@author: mpadilla
"""
_all__ = ["inputInt", "inputFloat", "inputString", "inputDate"]

from Helpers.DataTypeHelpers import *

def inputInt():
    for i in range (0,10000000):
        inputInteger=input("Enter an integer from 0 to 100: ")
        if isInt(inputInteger)==True:
            if int(inputInteger)<0 or int(inputInteger)>100:
                print("Please enter an integer in the range from 0 to 100: ")
                continue
            else:
                print(inputInteger)
                break
        else:
            print("This is not an integer")
            continue

        
def inputFloat():
    for i in range (0,100000):
        inputFlt=input("Enter a float from -10 to 1000: ")
        if isFloat(inputFlt)==True:
            if float(inputFlt)<-10 or float(inputFlt)>1000:
                print("Please enter a float in the range of -10 to 1000: ")
                continue
            else:
                print(inputFlt)
                break
        else:
            print("This is not a float")
            continue
def inputString():
    for i in range (0,1000000):
        inputStr=input("Enter a string in length 5 to 10: ")
        if len(inputStr)<5 or len(inputStr)>10:
            print("Please enter a string of the appropiate length from 5 to 10 characters long: ")
            continue
        else:
            print(inputStr)
            break

def inputDate():
    for i in range (0,10000000):
        inputDT=input("Enter a date: ")
        if  isDate(inputDT)==True:
            print(inputDT)
            break
        else: 
            print("Please enter a  valid date in YYYY-MM-DD format")
            continue
            
            
        