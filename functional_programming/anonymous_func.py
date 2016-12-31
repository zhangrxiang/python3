

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。


l = lambda x : x * x

print(l(2))



print(list(map(lambda x : x * (10 - x), range(1,10))))


def anonymous():
    return lambda x:x*2


anon = anonymous()
print(anon(10))


def build(x, y):
    return lambda: x * x + y * y


print(build(1, 2))
b = build(1, 2)
print(b())
print(build(1, 2)())

def count():
    fs = []
    for i in range(1, 4):
        # fs.append(lambda ii=i: ii*ii)
        fs.append(lambda: i * i)
    return fs
c1, c2, c3 = count()
print(c1())
print(c2())
print(c3())


def count():
    f = lambda j:lambda :j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()

print("*"*40)
print(f1())
print(f2())
print(f3())


ff = lambda j:lambda :j*j
fff = ff(10)
print(fff())
print(ff(10)())