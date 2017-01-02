# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:16:57 2016

@author: Ravi
"""

#Create a program that asks the user for a number and then prints out a list 
#of all the divisors of that number.
a=[]
num=int(input("Enter a number:"))
for i in range(1,num//2+1):
    if (num%i ==0):
        a.append(i)
a.append(num)
print(a)
