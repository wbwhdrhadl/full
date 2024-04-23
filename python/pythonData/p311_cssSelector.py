#!/usr/bin/env python

import re
from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'css01.html'

html = open(filename, encoding=myencoding)
soup = BeautifulSoup(html, myparser)

h1 = soup.select_one("div#cartoon > h1").string
print("h1 = ", h1)

li_list = soup.select("div#cartoon > ul.elements > li")
for li in li_list:
    print(li.string)
print('-'*50)

choice = lambda x : print(soup.select_one(x).string)

print('\n choice("#item5"):', end='')
choice("#item5")

print('\n choice("#item4"):', end='')
choice("#item4")

print('\n choice("ul > li#item3"):', end='')
choice("ul > li#item3")

print('\n choice("li[id=\'item1\']"):', end='')
choice("li[id=\'item1\']")

print('\nchoice("li:nth-of-type(4)") : ' ,end='')
choice("li:nth-of-type(4)")

print('\n choice("li")[1].string:',end='')
print(soup.find_all("li")[1].string)

print('\n choice("li")[3].string:',end='')
print(soup.find_all("li")[3].string)
print('-'*50)

mytag = soup.select_one('div#cartoon > ul.elements')
mystring = mytag.select_one('li:nth-of-type(3)').string
print(mystring)
print('-'*50)

mytag = soup.select_one('ul#itemlist')
mystring = mytag.select_one('li:nth-of-type(4)').string
print(mystring)
print('-'*50)

print(soup.select("#vegatables > li[class='us']")[0].string)
print(soup.select("#vegatables > li.us")[1].string)

result = soup.select('a[href$=".com"]')
for item in result:
    print(item['href'])
    print(item.string)

result = soup.select('a[href*=".daum"]')
for item in result:
    print(item['href'])
    print(item.string)
print('-'*50)

cond = {"id":"ko","class":"cn"}
print(soup.find("li",cond).string)
print('-'*50)
print(soup.find(id="vegatables").find("li", cond).string)
print('-' * 50)

print("# 정규 표현식으로 href에서 https인 것 추출")
li = soup.find_all(href=re.compile("^https://"))

for e in li:
    print(e['href'])

print(soup.select("#fruit > li")[0].string)
print('-'*50)
