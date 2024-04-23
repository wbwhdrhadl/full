#!/usr/bin/env python

from pandas import Series
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = "dataframeGraph.csv"
myframe = pd.read_csv(filename, encoding='euc-kr')
myframe = myframe.set_index('name')
print(myframe)

myframe.plot(kind='')