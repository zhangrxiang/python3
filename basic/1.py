a = 10 // 3
print(a)

a = 10 / 3
print(a)

a = 10 % 3
print(a)

a = 10 * 3
print(a)

a = 10 ** 3
print(a)

a = 10 + 3
print(a)

print(ord("A"))
print(ord("中"))
print(chr(ord("中")))

print("\u4e2d\u6587")

print("ABC".encode('ascii'))
print("ABC".encode('utf-8'))

print("中文".encode("utf-8"))

print(b'ABC'.decode("ascii"))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))
print("张荣响".encode("utf-8").decode("utf-8"))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len("卧槽")) # 2
print(len("卧槽".encode("utf-8"))) # 6

# %d	整数
print("整数 %d" % 10)
print("整数 %d---%d" % (10, 20))
# %f	浮点数
print("浮点数 %f---%f" % (10, 20.00))
print("浮点数 %.3f---%.4f" % (10, 20.00))
# %s	字符串
print("字符串 %s " % "这是一个字符串")
# %x	十六进制整数
print("十六进制整数 %x " % 100)
