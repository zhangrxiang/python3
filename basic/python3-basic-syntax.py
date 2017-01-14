#!/usr/bin/python3
# -*- coding:utf-8  -*-
import keyword

kwlist = keyword.kwlist
for i in range(0, len(kwlist), 10):
    print(kwlist[i:i+10])

a = b = c = d = 1
print(a, b, c, d)

a, b = 11, 22
print(a, b)

print(10 + 2j)
print(complex(10, 2))

str = "zhangrongxiang like houlingyan very much"
print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个个到倒数第二个的所有字符
print(str[0])       # 输出字符串第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
print(str + "!!!") # 连接字符串

# List（列表）
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号（+）是列表连接运算符，星号（*）是重复操作。
l = ["zing", "like", "hly", 666]
print(l)            # 输出完整列表
print(l[0])         # 输出列表第一个元素
print(l[1:3])       # 从第二个开始输出到第三个元素
print(l[2:])        # 输出从第三个元素开始的所有元素
print(l * 2)
l[0] = "zhangrxiang"
print(l)
# 1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。

# Tuple（元组）
# 元组的元素不能修改
t = tuple(l)
print(t)
print(t[0])          # 输出元组的第一个元素
print(t[1:3])        # 输出从第二个元素开始到第三个元素
print(t[2:])         # 输出从第三个元素开始的所有元素
print(t * 2)     # 输出两次元组

# string、list和tuple都属于sequence（序列）。
# 注意：
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。


# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号({})或者 set()函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

s = set(t)
print(s)

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象结合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
coder = {'name': 'zing','code': 1, 'site': 'github.com'}
print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(coder)          # 输出完整的字典
print(coder.keys())   # 输出所有键
print(coder.values()) # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典如下：

# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。

# Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
# 函数	描述
# int(x [,base])
# 将x转换为一个整数
# float(x)
# 将x转换到一个浮点数
# complex(real [,imag])
# 创建一个复数
# str(x)
# 将对象 x 转换为字符串
# repr(x)
# 将对象 x 转换为表达式字符串
# eval(str)
# 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)
# 将序列 s 转换为一个元组
# list(s)
# 将序列 s 转换为一个列表
# set(s)
# 转换为可变集合
# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)
# 转换为不可变集合
# chr(x)
# 将一个整数转换为一个字符
# unichr(x)
# 将一个整数转换为Unicode字符
# ord(x)
# 将一个字符转换为它的整数值
# hex(x)
# 将一个整数转换为一个十六进制字符串
# oct(x)
# 将一个整数转换为一个八进制字符串