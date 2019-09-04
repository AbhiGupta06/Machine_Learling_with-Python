# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:11:58 2019

@author: BSDU
"""

import pandas as pd

data = {'Gender': ['f', 'f', 'm'], 'Emp_id': ['2001', '2002', '2003' ], 'Age' :[10,20,30]}

df = pd.DataFrame(data,columns = ['Emp_id', 'Gender', 'Age'])

print(df)