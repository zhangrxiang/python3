import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(1))
print(my_abs(-1))
print(my_abs(1.1))
# print(my_abs("1"))

# raise TypeError("test")
# raise Warning("test")
# raise print("test")

def returnMore():
    return 1, 2, 3, 4

a, b, c, d = returnMore()
e = returnMore()
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(e)
print(returnMore())
print(type(returnMore()))
# print(c)


print(math.sqrt(4))

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s



print(power(2, 4))
print(power(2))

def add_end(L=[]):
    L.append('END')
    return L

# Python函数在定义的时候，默认参数L的值就被计算出来了，
# 即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
print(add_end())
print(add_end())
print(add_end())
print(add_end())
print(add_end())

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end2())
print(add_end2())
print(add_end2())
print(add_end2())
print(add_end2())



def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4))
print(calc(*[1, 2, 3]))

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

(person('Michael', 30))
(person('Michael', 30, city = 'wocao'))
(person('Michael', 30, city = 'wocao', fuck = 'fuck'))

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person2(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
(f1(*args, **kw))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
(f2(*args, **kw))


# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。