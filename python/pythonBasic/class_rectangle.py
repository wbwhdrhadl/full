#!/usr/bin/env python

class Rectangle:
    count = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def __add__(self, other):
        obj = Rectangle(self.width + other.height, self.height + other.height)
        return obj

    def calcArea(self):
        area = self.width * self.height
        return area
    def isSquare(rectWidth, resHeight):
        return rectWidth == rectheight

    def printConut(cls):
        print(cls.count)


