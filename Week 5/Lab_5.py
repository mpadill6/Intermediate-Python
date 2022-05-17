# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:26:26 2020

@author: mpadilla
"""
import sqlite3
from sqlite3 import Error
from random import randint
import pickle
people_db_file="sqlite.db" #Name of db to use
max_people= 500 #Number of records to create
from concurrent.futures import ThreadPoolExecutor

def create_people_database(db_file,max_people):
    conn=sqlite3.connect(db_file)
    with conn:
        sql_create_people_table=""" Create Table If Not Exists people (
            id integer Primary Key,
            first_name text NOT NULL,
            last_name text NOT NULL);"""
        cursor=conn.cursor()
        cursor.execute(sql_create_people_table)
        
        sql_truncate_people= "DELETE FROM people;"
        cursor.execute(sql_truncate_people)
        #people=generate_people(max_people)
        generate_people(max_people)
        sql_insert_person="INSERT INTO people(id,first_name,last_name) VALUES (?,?,?);"
        
        for person in people:
            #print(person)
            cursor.execute(sql_insert_person, person)
            #print(cursor.lastrowid)
        cursor.close()

last_names=[]
first_names=[]
people=[]
def generate_people(max_people):
    with open('LastNames.txt', 'r') as Lfilehandle:
        for line in Lfilehandle:
            last_names.append(line.rstrip())
    with open('FirstNames.txt', 'r') as Ffilehandle:
        for line in Ffilehandle:
            first_names.append(line.rstrip())    
    
    for i in range(max_people):
         my_tuple=(i,first_names[randint(0,len(last_names)-1)],last_names[randint(0,len(last_names)-1)])
         people.append(my_tuple)
    #print(people)
create_people_database(people_db_file,max_people)


class PersonDB():
    def __init__(self,db_file=''):
        self.db_file=db_file
    
    def __enter__(self):
        self.conn=sqlite3.connect(self.db_file)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

    def load_person(self,id):
        sql = "SELECT * FROM people WHERE id=?"
        cursor=self.conn.cursor()
        cursor.execute(sql,(id,))
        records=cursor.fetchall()
        result=(-1,'','') #id=-1, first_name='',last_name=''
        if records is not None and len(records)>0:
            result=records[0]
        cursor.close()
        return result

def test_PersonDB():

    with PersonDB(people_db_file) as db:
        print(db.load_person(10000)) #Should print the default
        print(db.load_person(122))
        print(db.load_person(300))
if __name__=="__main__":
    test_PersonDB()

def load_person(id,db_file):
    with PersonDB(db_file) as db:
        return db.load_person(id)
workers=[]  
def multiple_futures():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for x in range(10): 
            for i in range(max_people): workers.append(executor.submit(load_person,i, people_db_file))
        for w in workers:print(w.result())

multiple_futures()
