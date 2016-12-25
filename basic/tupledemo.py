a = 1, 2, 3
print(type(a))
print(a)
print(a.index(1))

print(a.count(1))
print(a[1])

b = a.__add__((4, 5, 6))
print(a)
print(b)

print(a.__contains__(1))
print(a.__len__())
iter__ = a.__iter__()
print(iter__)
for it in iter__:
    print(it)

for it in a:
    print(it)


a = ("aaa", "bbb", ("ccc", "ddd", ("eee", "fff")))
print(a)
print(a[0])
print(a[2][0])
print(a[2][2][0])
