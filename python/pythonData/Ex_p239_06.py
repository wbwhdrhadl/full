#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'ex802.csv'

myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name='도시(city)'

myframe.plot(kind='bar', rot=0, title='지역별 차량 등록 대수',legend=True)

print(myframe)
print('-'*50)

filename='dataFrameGraph02.csv'
plt.savefig(filename,dpi=400,box_inches='tight')
print(filename + 'Saved ...')

myframeT = myframe.T
print(myframeT)
print('-'*50)

myframeT.plot(kine='bar', rpt=0, title='지역별 차량 등록 대수')