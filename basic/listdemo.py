a = [1, 2, 3, 4, 5, 6]
print(type(a))
print(a)
a.append(7)
print(a)
a.append(8)
print(a)

b = a.copy()
print(b)
print(id(a), id(b)) #False

b.clear()
print(b) #[]
print(a)

print(a.count(1))
print(a.count(2))

a.extend([11, 22])
print(a)

print(a.index(1))
print(a.index(2))
print(len(a))
print(a)
# print(a.index(9))
# print(a.index(1, 2, 3))

a.insert(10, 100)
a.insert(11, 110)
a.insert(10, "110")
print(a)

print(a.pop()) # last value
print(a.pop(1)) # index value
print(a)

a.remove('110') # value
print(a)
a.remove(100)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

print(a[1])
print(a[1:])
print(a[-1])
print(a[-2])
print(a[-1:])
print(a[-2:])

print(a[1:3])
print(a[1:-3])

