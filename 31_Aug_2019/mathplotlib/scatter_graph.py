# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:32:46 2019

@author: BSDU
"""


from sklearn import datasets

iris = datasets.load_iris()

import matplotlib.pyplot as plt

x = iris.data[:,:4]

y = iris.target

plt.scatter(x[:, 2 ], x[:,2])

plt.xlabel("Petal Length")
plt.ylabel("Sepal Lenght")
