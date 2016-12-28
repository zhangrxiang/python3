import os

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

L = [x * x for x in range(1, 11)]
print(L)

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])
print([m + n for m in 'ABC' for n in 'ABC' if m != n])

print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录)

# 一边循环一边计算的机制，称为生成器 generator
g = (x * x for x in range(10))
print(type(g))

print(next(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print([x for x in g])


def fib(max):
    print("="*20+"fib begin"+"="*20)
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# print(fib(10))

def fib_yield(max):
    print("="*20+"fib begin"+"="*20)
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def odd():
    print('step 1')
    yield
    print('step 2')
    yield
    print('step 3')
    yield
o = odd()
next(o)
next(o)
next(o)
