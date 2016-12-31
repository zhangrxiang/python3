# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def calc_sum(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

print(calc_sum(1, 3, 5))


def lazy_sum(*args):
    def calc_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calc_sum


print(lazy_sum(1, 2, 3))
s = lazy_sum(1, 2, 3)
print(s())
print(lazy_sum(1, 2, 3)())

# 在函数lazy_sum中又定义了函数sum，并且，
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count2():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())
    return fs

f1, f2, f3 = count2()

print(f1)
print(f2)
print(f3)

def count3():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

print(count3())
f1, f2, f3 = count3()
print(f1())
print(f2())
print(f3())

L = []
g = lambda x:[1].append(x)
L.append(1)
L.append(2)
L.append(5)
print(L)




gg = lambda x : x*x
print(gg(2))
def ll():
    return [1, 2, 5]

xx1, xx2, xx3 = ll()
print(xx1)
print(xx2)
print(xx3)
