#!/usr/bin/env pyhon

from class_animal import *

dog = Dog('doggy')
print(dog.name)
dog.move()
dog.speak()

duck = Duck('donaid')
print(duck.name)
dog.move()
dog.speak()

zoo = [Dog('marry'), Duck('dduck')]

for z in zoo:
    print(z.name)
    z.speak()