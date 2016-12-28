from collections import Iterable

print(isinstance('abc', Iterable)) # str是否可迭代

print(isinstance([1, 2, 3], Iterable)) # list是否可迭代)

print(isinstance(123, Iterable))  # 整数是否可迭代

# 把一个list变成索引-元素对
enu = enumerate(['A', 'B', 'C'])
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9), ("x", "y")]:
    print(x, y)