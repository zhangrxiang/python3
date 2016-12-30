from functools import reduce


def f(x):return x * x

r = map(f ,[x for x in range(10)])
print(r)
print(next(r))
print(next(r))

while True:
    try:
        print(next(r))
    except StopIteration:
        break

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
def _abc(a):
    return -a

print(list(map(str, [x for x in range(10)])))
print(list(map(float, [x for x in range(10)])))
print(list(map(_abc, [x for x in range(10, 1, -1)])))

def add(a, b):
    return a ** b

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算

print(reduce(add, [2, 3, 5]))

def fn(x, y):
    print("*"*30)
    print(x)
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
for x in map(char2num, "13579"):
    print(x)

print(reduce(fn, map(char2num, '13579')))


def normalize(name=''):
    return name.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str_map(value=''):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': None}[value]
    pass
def str_reduce(a, b):
    pass


print(reduce(str_reduce, map(str_map, '123.456')))


def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return \
        reduce(lambda x, y: x * 10 + y,map(char2num, s[0:s.find('.')])) +\
        (reduce(lambda x, y: x / 10 + y, map(char2num, s[:s.find('.'):-1])))/10

print('str2float(\'123.456\') =', str2float('123.456'))