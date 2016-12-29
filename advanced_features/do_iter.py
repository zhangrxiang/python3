# 集合数据类型
# list、tuple、dict、set、str

# generator
# 生成器和带yield的generator function


# 用于for循环的对象统称为可迭代对象：Iterable
# 使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable, Iterator

# 可迭代对象 Iterable
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance(range(10), Iterable))


# 可以被next()函数调用并不断返回下一个值的对象称为迭代器： Iterator。
# False
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance(range(10), Iterator))

# True
print(isinstance((x for x in range(10)),Iterator))

# Iterable iter() Iterator


# Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，
# 但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，
# 只有在需要返回下一个数据时它才会计算。

# Iterator甚至可以表示一个无限大的数据流，
# 例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break