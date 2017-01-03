import types
from functools import reduce

from oop.extends import Animal, Dog

print(type(None))

print(type(abs))

print(type(list))

print(type(map))

print(type(reduce))

def fn():
    pass


if types.FunctionType == type(fn):
    print("FunctionType")

a = Animal()
d = Dog()

print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(a, Dog))


print(dir(Animal))


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print(hasattr(obj, "x"))
print(hasattr(obj, "y"))

setattr(obj, "y", "wocao")
hasattr(obj, "y")
print(obj.y)

attr = getattr(obj, "y")
print(attr)
try:
    attr = getattr(obj, "z")
    print(attr)
except:
    print("wocao 真没有 ")


print(hasattr(obj, "power"))