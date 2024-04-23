#!/usr/bin/env python

import numpy as np
from pandas import DataFrame

myindex = ['이순신','김유신','강감찬','광해군','연산군']
mycolumns = ['서울','부산','광주','목포','경주']

mylist =list(10* onedata for onedata in range(1,26))
print(mylist)

myframe = DataFrame(np.reshape(mylist,(5,5)), index=myindex, columns=mycolumns)
print(myframe)

print('\n 1 row data read of series')
result = myframe.iloc[1]
print(type(result))
print(result)

print('\n multi row data read of series')
result = myframe.iloc[[1,3]]
print(type(result))
print(result)

print('\n even row data read or series')
result = myframe.iloc[0::2]
print(type(result))
print(result)

print('\n 김유신 included row data read or series')
result = myframe.loc[['김유신']]
print(type(result))

print('\n 이순신, 김유신 included row data of DataFrame')
result = myframe.loc[['이순신','김유신']]
print(type(result))
print(result)

print()
print(myframe.index)
print('-'*50)

print('\n 이순신, 광주 실적 included row data of DataFrame')
result = myframe.loc[['이순신'],['광주']]
print(type(result))
print(result)

print('\n 연산군, 강감찬 / 광주 목포 실적 included row data of DataFrame')
result = myframe.loc[['연산군','강감찬'],['광주','목포']]
print(type(result))
print(result)

print('\n 이순신 ~ 강감찬 / 서울 ~ 목포 실적 included row data of DataFrame')
result = myframe.loc['이순신':'강감찬','서울':'목포']
print(type(result))
print(result)

print('\n 김유신 ~ 광해군 / 부산 실적 included row data of DataFrame')
result = myframe.loc['김유신':'광해군',['부산']]
print(type(result))
print(result)

print('\n Boolean Data Process')
result = myframe.loc[[False, True, True, False, True]]
print(result)

print('\n 부산 실적 <= 100')
result = myframe.loc[myframe['부산'] <= 100]
print(result)

print('\n 목포 실적 == 140')
result = myframe.loc[myframe['목포']== 140]
print(result)

cond1 = myframe['부산']>=70
cond2 = myframe['목포']>=140

print(type(cond1))
print('-'* 50)

df = DataFrame([cond1,cond2])
print(df)
print('-'* 50)

print(df.all())
print('-'* 50)

print(df.any())
print('-'* 50)

result = myframe.loc

print('\n lambda function')
result = myframe.loc[lambda df:df['광주']>=130]
print(result)

print('\n data set 30 : 이순신, 강감찬, 부산 실적')
myframe.loc[['이순신','강감찬']['부산']]=30
print(myframe)

print('\n data set 60 : 모든 사람 광주 실적')
myframe.loc[:,['광주']] = 60
print(myframe)
