# Slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L)

for l in L:
    print(l)

L = list(range(20))
print(L)

print(L[::10])
print(L[::-10])

print(L[1:10:2])

print(L[-2::-1])
print(L[-2:0:-1])
print(L[-2:0])
print(L[2:0])

print(L[2:-3:2])
print(L[-3:2:2])