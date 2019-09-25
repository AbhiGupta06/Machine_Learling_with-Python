# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:06:10 2019

@author: BSDU
"""

import pandas as pd

age = [18,20,23,19,18,22]
city = ['city A', 'city B', 'city B', 'city A', 'city C', 'city B']

data = pd.DataFrame({'age' : age, 'city': city})
print(data)

dummy_features = pd.get_dummies(data['city'])

data_age = pd.DataFrame(data=data, columns =['age'])

data_mod = pd.concat([data_age.reset_index(drop  = True), dummy_features],axis=1)
print(data_mod)