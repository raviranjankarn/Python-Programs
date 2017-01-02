# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:52:46 2016

@author: Ravi
"""
import os
import datetime

print(os.getcwd())
os.chdir('E:\\MUniversity\Python\Practice') #Change this directory to your local directory
print(os.getcwd())
current_time = datetime.datetime.now()
outFile = open('sample.txt', 'a+')
outFile.write('My first output file! at '+current_time.strftime('%d/%m/%Y  %H:%M:%S'))
outFile.write('\nHow are you doing')
name=input("What is your name:")
age=int(input("What is your age:"))
sex=input("What is your gender:")
outFile.write('\nname='+name+'\nage='+str(age)+'\nGender='+sex+'\n')
position=outFile.seek(0,0)
print(position)
for line in outFile:
    print(line)
outFile.close()
