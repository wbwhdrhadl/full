#!/usr/bin/env python

import pickle

class SmartPhone(object):
    def __init__(self, brand, maker, price):
        self.brand = brand
        self.market = maker
        self.price = price
    def __str__(self):
        return f'str: {self.brand} - {self.market} - {self.price}'

object =SmartPhone('IPhone", "Apple", 10000)
f =open("test.pickle" , "wb")
pickle.dump(object, f)
f.close()

f =open("test.pickle" , "rb")
object2 = pickle.load(f)
print(object2)
f.close()