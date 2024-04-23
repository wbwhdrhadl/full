#!/usr/bin/eny python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'mpg.csv'
myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

print(myframe['drv'].unique())

frame01 = myframe.loc[myframe['cyl'] == '1','drv']
frame01.index.name = '1'
print(frame01.head())
print('-'*50)

frame02 = myframe.loc[myframe['cyl'] == '4','drv']
frame02.index.name = '4'
print(frame02.head())
print('-'*50)

frame03 = myframe.loc[myframe['cyl'] == 'r','drv']
frame02.index.name = 'r'
print(frame03.head())
print('-'*50)

totalframe = pd.concat([frame01,frame02], axis=1, ignore_index=True)
totalframe.columns = ['1','4','r']
print(totalframe.head())
print('-'*50)

totalframe.plot(kind='box')
plt.xlabel('구동 방식')
plt.ylabel('주행 마일수')
plt.grid(False)
plt.title("고속도록 주행 마일수의 상자 수염")
filename = 'boxPlot02.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
print(filename + 'Saved ...')
plt.show()