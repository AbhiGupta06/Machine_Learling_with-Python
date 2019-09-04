# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:38:22 2019

@author: BSDU
"""
import random

num = random.randint(1,10)

#print(num)
list1= []


for i in range(1,15):
    num = random.randint(1,14)
    if num not in list1:
        list1.append(num)
        print(num)
    

        
        
        
        

