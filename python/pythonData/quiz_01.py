#!/usr/bin/env python

from bs4 import BeautifulSoup
from pandas import DataFrame as df
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

html = open('ex5-10.html','r',encoding='utf8')
soup = BeautifulSoup(html,'html.parser')

result=[]
tbody = soup.select_one('tbody')
tds = tbody.findAll('td')
for data in tds:
    result.append(data.text)
print(result)
print('-'*50)
mycolumns = ['이름', '국어', '영어']

myframe =df(np.reshape(np.array(result),(4,3)),columns=mycolumns)
myframe = myframe.set_index('이름')
print(myframe)
print('-'*50)

myframe.astype(float).plot(kind='line',title='Score',legend=True)
filename = 'scoreGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()




