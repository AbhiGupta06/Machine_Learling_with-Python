# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:48:03 2019

@author: BSDU
"""

from sklearn import datasets

iris = datasets.load_iris()

import matplotlib.pyplot as plt

x = iris.data[:,:1]

plt.boxplot(x)

plt.show()


plt.hist(x)




