# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:00:56 2019

@author: BSDU
"""

import pandas as pd

room_length = [18,20,18,17,10]

room_breadth = [20,20,10,11,19]

room_type =['Big', 'Normal', 'Big',  'Big', 'Noraml']

data = pd.DataFrame({'Lenght': room_length, 'Breadth': room_breadth, 'Tpye':room_type})
print(data)
data['Area'] = data['Lenght']* data['Breadth']
print(data)
