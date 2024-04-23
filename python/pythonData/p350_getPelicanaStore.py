#!/usr/bin/env python

from itertools import count
from p340_ChickenUtil import ChickenStore

brandName = 'pelicana'
base_url = 'https://www.pelicana.co.kr/store/store'

def getData():
    saveData = []

    for page_idx in count():
        url = base_url + '?page=' +str(page_idx +1)
        print(url)
        chkenStore = ChickenStore(brandName, url)

getData()