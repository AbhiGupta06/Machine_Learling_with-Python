# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:14:56 2019

@author: BSDU
"""

import pandas as pd

from sklearn import preprocessing

marks_science = [78,56,87,91,45,62]

marks_maths = [75,62,90,95,42,57]

grade = ['A', 'B', 'C', 'A', 'D', 'B']

data = pd.DataFrame({'Science Marks': marks_science, 'Maths marks': marks_maths, 'Total Grade': grade})

print(data)

le = preprocessing.LabelEncoder()
le.fit(data['Total Grade'])
data['Total Grade'] = le.transform(data['Total Grade'])
print(data)