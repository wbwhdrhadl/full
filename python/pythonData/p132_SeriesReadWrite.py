#!/usr/bin/env python

from pandas import Series

myindex = ['용산구', '마포구', '영등포구','서대문구', '광진구', '은평구', '서초구']
mylist = [50, 60, 40, 80, 70, 30, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)

print('\n read value')
print(myseries[['서대문구']])

print('\n slicing label name')
print(myseries['서대문구':'은평구'])

print('\n read data')
print(myseries[['서대문구','서초구']])

print('\n read index')
# print(myseries[[2]])
print(myseries.iloc[2])

print('\n read using index 0, 2, 4')
print(myseries.iloc[[0,2,4]])

print('\n slicing using index')
print(myseries[0:5:2])

myseries[2]=90
myseries[2:5]=33
myseries[['용산구','서대문구']]=55
print('\n Series list')
print(myseries)

myseries[0::2]=80
print('\n Series List')
print(myseries)