#!/usr/bin/env python

def gcd(a, b):
    if a<b:
        a,b = b,a
    print("gcd",(a,b))
    while b!=0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd1 = Gcd(a,b)
print(f'gcd({a},{b}) of {a},{b} : {gcd1.gcd()}')