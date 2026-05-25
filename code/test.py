import os, sys
import math

x = 1
y = 2
z = x + y


def add(a, b):
    return a + b


def greet(name):
    print("Hello " + name)


class myClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getSum(self):
        return self.x + self.y


result = add(x, y)
obj = myClass(1, 2)
print(obj.getSum())
