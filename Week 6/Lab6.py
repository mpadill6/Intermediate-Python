# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:10:30 2020

@author: mpadilla
"""

from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep

max_customers_in_bank=10
max_customers=30
max_tellers=3
teller_timeout=10
class Customer():
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        print(f"{'self.name'}")

class Teller():
    def __init__(self,name):
        self.name=name
    def __str__():
       print( f"{'self.name'}")

def bankprint(lock,msg):
    with lock:
        print(msg)

def wait_outside_bank(i,customer,guard,teller_line,printlock):
        print(f"(C) Customer{i} waiting outside bank\n")
        guard.acquire()
        bankprint(printlock, f"<G> Security guard letting Customer{i} into the bank \n")
        bankprint(printlock, f"(C) Customer{i} getting in line \n")
        teller_line.put(f"Customer {i}")
       
            
def teller_job(j, teller, guard, teller_line, printlock):
        bankprint(printlock, f"[T] Teller{j} has started working \n")
        try: 
           bankprint(printlock, f"[T] Teller{j} is helping {teller_line.get(timeout=teller_timeout)} \n") 
           sleep(randint(1,4))
           bankprint(printlock, f"[T] Teller{j} is done helping {teller_line.get(timeout=teller_timeout)} \n")
           bankprint(printlock, f"<G> Security guard letting {teller_line.get(timeout=teller_timeout)} outside the bank \n")
           guard.release()
          
        except teller_line.Empty:
            bankprint(printlock, f"[T] Nobody in line, Teller{j} is going on break \n")
        finally:
            pass
if __name__=="__main__":
    printlock=Lock()
    teller_line=Queue(maxsize=max_customers_in_bank)
    guard=Semaphore(max_customers_in_bank)
    bankprint(printlock, "<G> Security guard starting their shift")
    bankprint(printlock, "*B* Bank Open")
    Customer=[Thread (name=f"Customer{i}", target= wait_outside_bank, args=(i,Customer,guard,teller_line,printlock)) for i in range(1,max_customers+1)]
    sleep(5)
    bankprint(printlock, "*B* Tellers Starting work")
    Teller=[Thread (name=f"Teller{j}", target=teller_job, args=(j,Teller,guard,teller_line,printlock)) for j in range(1,max_tellers+1)]
    
    for c in Customer:
        c.start()
         
    for t in Teller:
        t.start()
        
    for c in Customer:
        c.join()
        
    for t in Teller:
        t.join()
    bankprint(printlock, "*B* Bank is closed")       


        
