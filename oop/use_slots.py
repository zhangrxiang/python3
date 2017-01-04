from types import MethodType


class Student:
    def __init__(self, name):
        self.name = name
    pass


s = Student("zing")
print(s.name)
def setName(self, name):
    self.name = name
def setAge(self, age):
    self.age = age

s.setName = MethodType(setName, s)
s.setName = "zhangrxiang"
s.setAge = MethodType(setAge, s)
s.setAge(100)
print(s.name)
print(s.age)


class Man:
    __slots__ = ('name', 'age')

m = Man
m.name = 'zing'
m.age = 21
m.score = 11
