#!/usr/bin/env python

import random

def gcd(a, b):
    print("gcd", (a, b))
    while b != 0:
        r=a%b
        a=b
        b=r
    return a
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

print(f'gcd({a}, {b}) = {gcd(a, b)}')