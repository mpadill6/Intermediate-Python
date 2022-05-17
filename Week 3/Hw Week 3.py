# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:32:08 2020

@author: mpadilla
"""
#Part I
class Student(object):
    def __init__(self,id,firstname,lastname, courses={}):
        self.id=id
        self.firstname=firstname
        self.lastname=lastname
        self.courses=courses
    
    def addCourse(self,course,score):
        self.score=score
        self.course=course
        assert type(self.score) is float or type(self.score) is int, "Value must be int or float"
        assert type(self.course) is str, "Course name must be a string"
        self.courses[self.course]=self.score
        
    def addCourses(self,courses_added):
        assert type(courses_added) is dict, "Your entry is not dictionary format"
        self.courses.update(courses_added)
        
    def gpa(self):
        if self.courses=={}:
            self.GPA=0.00
        else:
            self.GPA=(sum(self.courses.values())/(len(self.courses.values())))
            return f"{self.GPA:.2f}"
        
    def __str__(self):
  
        return f"{self.id:<15} {self.lastname:<20} {self.firstname:<25} {str(self.gpa()):<30} {str(self.courses.keys()).replace('dict_keys',''):<35}"

    def __repr__(self):
        return f"{self.id}, {self.lastname}, {self.firstname}, {self.courses}"        

            
def header():
    print( f"{'ID':<15} {'Last Name':<20} {'First Name':<25} {'GPA':<30} {'Courses':<35}")
    print( "=" * 180)



#Part II
students=[]
s1=Student('123456','Johnnie' ,'Smith', {'CSE-101':3.50, 'CSE-102': 3.00, 'CSE-201' : 4.00, 'CSE-220':3.75, 'CSE-325':4.00})
s2=Student('234567', 'Jamie', 'Strauss', {'CSE-101': 3.00, 'CSE-103':3.50, 'CSE-202':3.25,'CSE-220':4.00, 'CSE-401':4.00})
s3=Student('345678', 'Jack', "O'Neill", {'CSE-101':2.50, 'CSE-102':3.50, 'CSE-103':3.00,'CSE-104':4.00})
s4=Student('456789', 'Susie', 'Marks', {'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302':3.00, 'CSE-310':4.00})



s5=Student('567890', 'Frank', 'Marks',{})
s5.addCourse('CSE-102',4.00)
s5.addCourse('CSE-104',3.50)
s5.addCourse('CSE-201',2.50)
s5.addCourse('CSE-202',3.50)
s5.addCourse('CSE-203',3.00)


s6=Student('654321', 'Annie', 'Marks',{})
s6.addCourse('CSE-101', 4.00)
s6.addCourse('CSE-102', 4.00)
s6.addCourse('CSE-103', 3.50)
s6.addCourse('CSE-201', 4.00)
s6.addCourse('CSE-203', 4.00)

s7=Student('456987', 'John', 'Smith',{})
s7.addCourse('CSE-101',2.50)
s7.addCourse('CSE-103',3.00)
s7.addCourse('CSE-210',3.50)
s7.addCourse('CSE-260',4.00)



s8=Student('987456', 'Judy', 'Smith',{})
s8.addCourses({'CSE-102':4.00, 'CSE-103':4.00, 'CSE-201':3.00, 'CSE-210':3.50, 'CSE-310':4.00})

s9=Student('111354', 'Kelly', 'Williams',{})
s9.addCourses({'CSE-101':3.50, 'CSE-102':3.50, 'CSE-201':3.00, 'CSE-202':3.50, 'CSE-203':3.50})

s10=Student('995511', 'Brad', 'Williams',{})
s10.addCourses({'CSE-102':3.00, 'CSE-110':3.50, 'CSE-125':3.50, 'CSE-201':4.00, 'CSE-203':3.00})



students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)
students.append(s5)
students.append(s6)
students.append(s7)
students.append(s8)
students.append(s9)
students.append(s10)

header()
def printStudents():
    for i in range (0,len(students)):
        print(students[i])
    
printStudents()
print('\n')

#Part III

#Query 1

print('Query by last name in ascending order')
header()
students.sort(key=lambda row:(row.lastname, row.firstname))
for p in students: print(p)

print('\n')
print('Query by first name in ascending order')
header()
students.sort(key=lambda row:(row.firstname, row.lastname))
for p in students: print(p)

#Query 2
print('\n')
print('Query by GPA in descending order')
header()
students.sort(key=lambda row:(row.gpa()),reverse=True)
for p in students: print(p)
print('\n')
#Query 3
unique=set()
for i in range (0,len(students)):
    a=set(students[i].courses.keys())
    unique=unique.union(a)
print('Set of unique courses')
print(unique)
print('Number of unique courses:', len(unique))

print('\n')

#Query 4
print("Students who took CSE-201")
for i in range (0,len(students)):
    a=set(students[i].courses.keys())
    if 'CSE-201' in a:
        print(f"{students[i].firstname} , {students[i].lastname}")

print('\n')

#Query 5
print("List of Honor Roll (GPA>=3.5)")
for i in range (0,len(students)):
    if students[i].GPA>=3.5:
        print(f"{students[i].firstname} , {students[i].lastname}")
