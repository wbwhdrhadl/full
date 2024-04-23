#!/usr/bin/env python

class Person(object):
    total = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getname(self):
        return self.name
    def getAge(self):
        return self.age
my =Person('John', 23)
print(my.name)
print(my.age)
print(my.getname())
print(my.getAge())
print(my.total)

you = Person('Jack', 25)
print(you.getname())
print(you.getAge())
print(you.total)

