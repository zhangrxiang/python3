# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/8
# Time: 14:40
# File: 
# Project: python3
# Location: Wuxi
import os
from datetime import datetime
from time import sleep

file = None
try:
    file = open("test.txt", "r")
except:
    print("no this file")

if(file!=None):
    readable = file.readable()
    print(readable)
    '''从文件读取指定的字节数，如果未给定或为负则读取所有。'''
    read = file.read()
    print('-'*20+'read'+'-'*20)
    print(read)

    '''seek() 方法用于移动文件读取指针到指定位置。'''
    file.seek(0, 0)

    readline = file.readline(10)
    print('-' * 20 + 'readline' + '-' * 20)
    print(readline)

    '''返回文件当前位置。'''
    print(file.tell())
    next(file)
    encoding = file.encoding
    print(encoding)

    file.seek(0, 0)

    '''读取所有行并返回列表，若给定sizeint>0，
    返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大,
    因为需要填充缓冲区。'''
    readlines = file.readlines()
    print('-' * 20 + 'readlines' + '-' * 20)
    print(readlines)

    '''刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。'''
    file.flush()

    '''关闭文件。关闭后文件不能再进行读写操作。'''
    file.close()

f = open("test.txt", "a+")
writable = f.writable()
print(writable)
for i in range(10):
    f.write("\nthis is test by coding -->"+str(datetime.now()))
    sleep(1)

f_read = f.readline()
print(f_read)

f.close()

# file.isatty()
# 如果文件连接到一个终端设备返回 True，否则返回 False。

# file.truncate([size])
# 截取文件，截取的字节通过size指定，默认为当前文件位置。

# file.writelines(sequence)
# 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。