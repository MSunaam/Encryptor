#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 20:02:12 2021

@author: muhammadsunaam
"""
list1=[]

def separate(num): #adding numbers in list
    for i in range(str_len):
        list1.append(num[i])
    return list1
  
#input number from user as string
num = input("Please enter a number to decrypt ")
#finding length of string number
str_len = len(num)
#calling separate function and storing it in list1
list1 = separate(num)
#converting list1 to integer
list1 = list(map(int,list1))
#encrypting
for i in range(len(list1)):
    list1[i] = (list1[i]+3)%10
#swapping places
for i in range(0,str_len,4):
    if i+2 < str_len:
        list1[i],list1[i+2]=list1[i+2],list1[i]
    if i+3<str_len:
        list1[i+1],list1[i+3]=list1[i+3],list1[i+1]
#making integer from list
for i in range(str_len):
    print(list1[i],end="")