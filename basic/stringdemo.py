a = 'abcdf'
print(a)
print(a[1])
for i in a:
    print(i)

# a[0] = '0'
print(a.upper())
print(a)
print(a.count("a"))
print(a.index("a"))
try:
    index = a.index("a", 1, 2)
except:
    print("卧槽，出错了")

'''首字母大写'''
print(a.capitalize())

print(a.casefold())

print(a.encode())
print(a.center(2, '@'))
print(a.endswith('f'))
print(a.expandtabs())

print(a.find("bc"))

#?
print(a.format('{{}}'))

print(a.isalnum())
print(a.isdecimal())

''' Return True if S is a valid identifier according
        to the language definition.'''
print(a.isidentifier())

print(a.islower())

'''Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.'''
print(a.isprintable())

print(a.isspace())

''' Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.'''
print(a.join([x for x in ["111", "222", '333']]))

# 1
# capitalize()
# 将字符串的第一个字符转换为大写
# 2
# center(width, fillchar)
#
# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
# 3
# count(str, beg= 0,end=len(string))
#
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# 4
# bytes.decode(encoding="utf-8", errors="strict")
#
# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
# 5
# encode(encoding='UTF-8',errors='strict')
#
# 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# 6
# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
# 7
# expandtabs(tabsize=8)
#
print("         asd sad     asd".expandtabs())
# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
# 8
# find(str, beg=0 end=len(string))
#
# 检测 str 是否包含在字符串中 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# 9
# index(str, beg=0, end=len(string))
#
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
# 10
# isalnum()
#
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
# 11
# isalpha()
#
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
# 12
# isdigit()
#
# 如果字符串只包含数字则返回 True 否则返回 False..
# 13
# islower()
#
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# 14
# isnumeric()
#
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
# 15
# isspace()
#
print(" ".isspace())
# 如果字符串中只包含空格，则返回 True，否则返回 False.
# 16
# istitle()
#
# 如果字符串是标题化的(见 title())则返回 True，否则返回 False
print("".istitle())
print("AVS".istitle())

# 17
# isupper()
#
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# 18
# join(seq)
#
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# 19
# len(string)
#
# 返回字符串长度
# 20
# ljust(width[, fillchar])
#
# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
print("    asd".ljust(5, "1"))
print("    asd".ljust(1, "v"))
# 21
# lower()
#
# 转换字符串中所有大写字符为小写.
# 22
# lstrip()
#
# 截掉字符串左边的空格
print("  sdf".lstrip())
# 23
# maketrans()
#
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 24
# max(str)
#
# 返回字符串 str 中最大的字母。
# 25
# min(str)
#
# 返回字符串 str 中最小的字母。
# 26
# replace(old, new [, max])
#
# 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
# 27
# rfind(str, beg=0,end=len(string))
#
# 类似于 find()函数，不过是从右边开始查找.
# 28
# rindex( str, beg=0, end=len(string))
#
# 类似于 index()，不过是从右边开始.
# 29
# rjust(width,[, fillchar])
#
# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
# 30
# rstrip()
#
# 删除字符串字符串末尾的空格.
# 31
# split(str="", num=string.count(str))
#
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
# 32
# splitlines( num=string.count('\n'))
#
# 按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
# 33
# startswith(str, beg=0,end=len(string))
#
# 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
# 34
# strip([chars])
#
# 在字符串上执行 lstrip()和 rstrip()
# 35
# swapcase()
#
# 将字符串中大写转换为小写，小写转换为大写
# 36
# title()
#
# 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# 37
# translate(table, deletechars="")
#
# 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
# 38
# upper()
#
# 转换字符串中的小写字母为大写
# 39
# zfill (width)
#
# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
# 40
# isdecimal()
#
# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。