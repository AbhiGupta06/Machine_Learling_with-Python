# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:11:12 2019

@author: BSDU
"""

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

x = pd.DataFrame(iris.data)
x.columns = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Wid"]

print("Shape:\n", x.shape)
print("Head:\n", x.head(5))
print(x.describe)
print(x.corr)
print(x.skew)

#
#df = pd.read_csv("E:\\Data.csv")
#print("Shape:\n",df.shape)
#print("Head:\n", df.head(5))
#print(df.describe)
#print(df.corr)
#print(df.skew)






