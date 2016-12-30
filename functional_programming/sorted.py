print(sorted([334, 23, 4564, 234, 2367]))

print(sorted([36, 5, -12, 9, -21], key=abs))

def xx(x):
    if x < 0:
        x = -x
    if x == 1:
        return 1
    return x + xx(x-1)

print(xx(10))

def compare(x):
    if x < 0:
        return -x
    return x
def compare2(x):
    return x % 5

print(sorted([36, -345, 12, 9, -21], key=compare))
print(sorted([36, -345, 12, 9, -21], key=xx))
print(sorted([36, -345, 12, 9, -21], key=compare2))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

def compare3(x=()):
    return x[0]

def by_score(t=()):
    return t[1]


print(sorted(L, key=compare3, reverse=True))
print(sorted(L, key=by_score, reverse=False))