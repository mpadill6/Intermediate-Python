# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:46:55 2020

@author: mpadilla
"""
#Part I

from fractions import Fraction
from decimal import*
pi50=Decimal("3.14159265358979323846264338327950288419716939937510")
class LeibnizPiIterator:
    
    def __init__(self, max):
        self.max=max
        pass
    
    def __iter__(self):
        self.fraction=Fraction(0,1)
        self.n=1
        self.add__next=True
        self.index=0
        return self

    
    def __next__(self):
            if self.index>=self.max:
                raise StopIteration
            else:
                if self.add__next==True:
                    self.fraction=self.fraction+Fraction(4,self.n)
                    self.add__next=False
                    self.n+=2
                    self.index+=1
                else:
                    self.fraction=self.fraction-Fraction(4,self.n)
                    self.add__next=True
                    self.n+=2
                    self.index+=1
            if self.index % 10000==0: print(float(self.fraction))
            return  float(self.fraction)
            
        
for x in LeibnizPiIterator(100000):
    pass
print("Leibniz pi after 100,000 iterations is", x)
print("Leibniz Difference: ", float(pi50)-x)
   

for y in LeibnizPiIterator(10000000):
    pass
print("pi after 10,000,000 iterations is", y)
print("Difference: ", float(pi50)-y)
        
#%%
#Part II

from fractions import Fraction
from decimal import*
pi50=Decimal("3.14159265358979323846264338327950288419716939937510")
class NikalanthaPiIterator:
    
    def __init__(self, max):
        self.max=max
        pass
    
    def __iter__(self):
        self.fraction=Fraction(3,1)
        self.d1=2
        self.d2=3
        self.d3=4
        self.operand=Fraction(4,(self.d1*self.d2*self.d3))
        self.add__next=True
        self.index=0
        return self

    
    def __next__(self):
            if self.index>=self.max:
                raise StopIteration
            else:
                if self.index==0:
                    self.index+=1
                else:
                    if self.add__next==True:
                        self.fraction=self.fraction+self.operand
                        self.add__next=False
                        self.d1+=2
                        self.d2+=2
                        self.d3+=2
                        self.operand=Fraction(4,(self.d1*self.d2*self.d3))
                        self.index+=1
                    else:
                        self.fraction=self.fraction-self.operand
                        self.add__next=True
                        self.d1+=2
                        self.d2+=2
                        self.d3+=2
                        self.operand=Fraction(4,(self.d1*self.d2*self.d3))
                        self.index+=1
            if self.index % 10000==0: print(float(self.fraction))
            return  float(self.fraction)
            
        
for a in NikalanthaPiIterator(100000):
    pass
print("Nikalantha pi after 100,000 iterations is", a)
print("Nikalantha Difference: ", float(pi50)-a)
   

for b in NikalanthaPiIterator(10000000):
    pass
print("pi after 10,000,000 iterations is", b)
print("Difference: ", float(pi50)-b)

#%%
#Part III
from functools import reduce
def compose(*functions):
    return reduce(lambda f, g:lambda x: g(f(x)), functions)
#Functions 
def milesToYards(value):
    return value*1760
def yardsToMiles(value):
    return value/1760
def yardsToFeet(value):
    return value*3
def feetToYards(value):
    return value/3
def feetToInches(value):
    return value*12
def inchesToFeet(value):
    return value/12
def inchesToCm(value):
    return value*2.54
def cmToInches(value):
    return value/2.54
def cmToMeters(value):
    return value/100
def metersToCm (value):
    return value*100
def metersToKm(value):
    return value/1000
def kmToMeters(value):
    return value*1000
def kmToAu (value):
    return value/149597870.7
def auToKm (value):
    return value*149597870.7
def auToLy (value):
    return value/63241.07708426628026865358
def lyToAu (value):
    return value*63241.07708426628026865358

convertMilestoInches=compose(milesToYards,yardsToFeet,feetToInches)
inches=convertMilestoInches(2)
print ("2 miles is", inches, "inches")

convertFeettoMeters=compose(feetToInches,inchesToCm,cmToMeters)
meters=convertFeettoMeters(5)
print("5 feet is", meters, "meters")

convertMeterstoInches=compose(metersToCm,cmToInches)
inches=convertMeterstoInches(1)
print("1 meter is", inches,"inches")

convertMilestoKm=compose(milesToYards,yardsToFeet,feetToInches,inchesToCm,cmToMeters,metersToKm)
kilometers=convertMilestoKm(10)
print("1 mile is", kilometers, "kilometers")

convertKmtoMiles=compose(kmToMeters,metersToCm,cmToInches,inchesToFeet,feetToYards,yardsToMiles)
miles=convertKmtoMiles(1)
print("1 kilometer is", miles, "miles")

convertKmtoInches=compose(kmToMeters,metersToCm,cmToInches)
inches=convertKmtoInches(12.7)
print("12 kilometers is", inches, "inches")

convertInchestoKm=compose(inchesToCm,cmToMeters,metersToKm)
kilometers=convertInchestoKm(500000)
print("500000 inches is", kilometers, "kilometers")

convertMeterstoLy=compose(metersToKm,kmToAu,auToLy)
lightyears=convertMeterstoLy(9460730472580800)
print("9460730472580800 meters is", lightyears, "light years")

#Extra Credit Conversions
def cmToMm(value):
    return value*10
def mmToCm(value):
    return value/10
def mmToUm(value):
    return value*1000
def umToMm(value):
    return value/1000
def umToA(value):
    return value*10000
def AToUm(value):
    return value/10000

convertFeetToMm=compose(feetToInches,inchesToCm,cmToMm)
mm=convertFeetToMm(1)
print("1 foot is", mm, "mm")

convertInchestoA=compose(inchesToCm,cmToMm,mmToUm,umToA)
A=convertInchestoA(1)
print("1 inch is", A, "Angstrom")

convertUmtoInches=compose(umToMm,mmToCm,cmToInches)
inches=convertUmtoInches(1000)
print("1000 um is", inches, "inches")


