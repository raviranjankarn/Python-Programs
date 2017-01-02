# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:33:11 2016

@author: Ravi
"""

#Ask the user for a number. Depending on whether the number is even or odd, 
#print out an appropriate message to the user.

num=int(input("Enter a number:"))
if (num%2==0):
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")