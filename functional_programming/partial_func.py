import functools

print(int("11111111", 2))
print(int("22222222", 3))
print(int("7777", 8))
print(int("77", 8))

partialInt = functools.partial(int, base=2)
print(partialInt("1001001"))
kw = {'base': 2}
print(int("1010101", **kw))

print(max(1, 3, 77, 32, 123, 45))

max2 = functools.partial(max, 20)
print(max2(2, 4, 5, 30))
