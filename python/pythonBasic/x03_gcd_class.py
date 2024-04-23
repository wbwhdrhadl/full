#!/usr/bin/env python

class Gcd(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gcd(self):
        print("gcd",(self.a, self.b))
        while self.b != 0:
            r = self.a % self.b
            self.a = self.b
            self.b = r
        return self.a

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

data = Gcd(a, b)
print(f'gcd({a}, {b}) = {data.gcd()}')