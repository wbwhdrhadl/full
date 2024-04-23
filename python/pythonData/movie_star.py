#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

url = 'https://www.moviechart.co.kr/rank/boxoffice'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
mydata0 = [i for i in range(1, 20)]
info = soup.find_all('td','title')
audience = soup.select("td.audience")
title=[]

for i in info:
    title.append(i.text)
print(title)



audience1 = []

for i in audience:
    audience1.append(i.text)
print(audience1)

# mydata0 = [i for i in range(1,20)]
#
# result = []
#
# title =soup.select("strong.title")
# for i in title:
#     result.append(i.text)
# mydata2 = result
#
# result = []
# score = soup.select("span.percent")
# for i in score:
#     result.append(i.text)
# mydata3 = result
#
# result = []
# release =soup.select("span > strong")
# for i in release:
#     result.append(i.text.strip()[0:10])
# mydata4 = result
#
# mycolumn = ['순위', '제목', '평점', '예매율', '개봉일']
#
#
# df = pd.DataFrame(data = list(zip(mydata0,mydata2,mydata3,mydata4)),columns=mycolumn)
# df = df.set_index(keys=['순위'])
# print(df)
# print('-'*40)
#
# filename = 'cgvMovie.csx'


