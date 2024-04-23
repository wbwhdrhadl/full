#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

url = 'http://www.cgv.co.kr/movies/'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

info = soup.findAll('div', attrs={'class':'sect-movie-chart'})

mydata0 = [i for i in range(1,20)]

result = []

title =soup.select("strong.title")
for i in title:
    result.append(i.text)
mydata2 = result

result = []
score = soup.select("span.percent")
for i in score:
    result.append(i.text)
mydata3 = result

result = []
release =soup.select("span > strong")
for i in release:
    result.append(i.text.strip()[0:10])
mydata4 = result

mycolumn = ['순위', '제목', '평점', '예매율', '개봉일']


df = pd.DataFrame(data = list(zip(mydata0,mydata2,mydata3,mydata4)),columns=mycolumn)
df = df.set_index(keys=['순위'])
print(df)
print('-'*40)

filename = 'cgvMovie.csx'


# info1 = soup.findAll('strong', attrs={'class':'title'})
# info2 = soup.select("div[class='score'] > strong.percent > span")
# info3 = soup.select("span[class='txt-info'] > strong")
# info4 = soup.select("div[class='egg-gage small'] > span.percent")
# info5 = soup.select("div[class='box-contents']")
# info6 = soup.findAll('strong', attrs={'class':'percent' })
# rank = []
# name = []
# score = []
# rate = []
# opendate = []
#
# for n in info1:
#     name.append(n.text)
# print(name)
#
# total = len(name)
# for p in range(0,total):
#     rank.append(p+1)
#     p+=1
# print(rank)
#
# for l in info4:
#     score.append(l.text)
# print(score)
#
# for m in info2:
#     rate.append(m.text)
# print(rate)
#
# for k in info3:
#     opendate.append(k.get_text(strip=True))
# print(opendate)
#
# print('-' * 50)
#
# print(info6)
