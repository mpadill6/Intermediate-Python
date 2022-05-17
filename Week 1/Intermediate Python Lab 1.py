# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 21:53:14 2020

@author: mpadilla
"""
#Lab 1 Mario Padilla: Intermediate Python
#Part 1 Palindrome

string=input("Please enter a string to check for palindrome:")
word=string.replace(" ","") #remove whitespaces
word=word.lower() #change all letters to lowercase to avoid case mismatch
if len(word)%2==0:   #situation where string is even length
    a=1
    match=0
    for i in range(0,int(len(word)/2)):
        if word[i]==word[-a]:
            match+=1
            a+=1
        else:
           a+=1
           pass
    if match==int(len(word)/2):  #if all iterations of loop give a match, then palindrome is found
        print(f"The string ''{string}'' is a palindrome!")
    else:                        #if any iteration of the loop doesn't give a match, it is not a palindrome
        print(f"The string ''{string}'' is not a palindrome!")
else:            #situation where string length is odd
    a=1
    match=0
    for i in range(0,int(len(word)//2)+1):
        if word[i]==word[-a]:
            match+=1
            a+=1
        else:
           a+=1
           pass
    if match==int(len(word)//2)+1: #if all iterations of loop give a match, then palindrome is found
        print(f"The string ''{string}'' is a palindrome!")
    else:                          #if any iteration of the loop doesn't give a match, it is not a palindrome
        print(f"The string ''{string}'' is not a palindrome!")
#%%
#Part 2 Password Strength
password=input("Please enter your desired password:")
score=0 #initial score

#Set of conditionals with break statetements to check for lower,upper,number and symbol
for i in range(0,len(password)):
    if password[i].islower()==True:
        score+=1
        break
for i in range(0,len(password)):
    if password[i].isupper()==True:
        score+=1
        break
for i in range(0,len(password)):    
    if password[i].isnumeric()==True:
        score+=1
        break
for i in range(0,len(password)):    
    if password[i].isalnum()==False:
        score+=1
        break
if len(password)==8: #conditional if length is 8
    score+=1
if len(password)>8 and len(password)<16: #condtitional if length is higher than or equal to 8 but lower than 16 give 2 total points for length
    score+=2
if len(password)>8 and len(password)>=16:#Condiitional if length is 16 or higher, give 3 total points for length
    score+=3
print("Your password score is:", score) #Output final assword score
#%%
#Part 3 Compound Interest
principal=float(input("Please enter the starting principal balance between 1.00-1000000.00: "))
percentage=float(input("Please enter your desired interest rate (ex: 4.5): "))
duration=int(input("Enter term in years (ex:10): "))
apr=(percentage/100)
year_title="Year"
interest_title="Interest"
balance_title="Balance"
print(f"{year_title:<20} {interest_title} {balance_title:>20}")
print("="*60)
for i in range(1,duration+1):
    interest=principal*apr
    principal=principal+interest
    print(f"{i:<20}  ${interest:,.2f}           ${principal:>10,.2f}")






