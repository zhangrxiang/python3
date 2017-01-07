#!/usr/bin/python3

# 操作系统接口
import os
# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import random
import shutil

# 文件通配符
import glob

# 命令行参数
import sys

# 字符串正则匹配
import re

# 数学
import math

# 访问 互联网
import unittest
import urllib

# 日期和时间
import datetime

# 数据压缩
import gzip
import zlib

# 性能度量
import timeit

# 测试模块
import doctest


from time import sleep
from urllib.request import urlopen

from builtins import print

print(os.getcwd())
print(os.times())
print(os.getlogin())

shutil.copy("python3-stdlib.py","python3-stdlib.txt")
# sleep(5)
shutil.move("python3-stdlib.txt","stdlib.txt")

print(glob.glob('*.py'))
print(glob.escape("py"))

print(sys.argv)
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.stdout.write('stdout, log file not found starting a new one\n')

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print('tea for too'.replace('too', 'two'))

print(math.cos(math.pi / 4))
print(math.log(1024, 2))

print(random.choice(['apple', 'pear', 'banana']))
print(random.choices(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10)) # sampling without replacement)
print(random.random())
print(random.randrange(6))

# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     print("wori")
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)
#         print("wocao")

now = datetime.date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = datetime.date(1994, 9, 18)
age = now - birthday
print(age.days) #8147
print(age.days/363) #22.443526170798897
print((10000-age.days)/365)
print((8888-age.days)/365)

s = b'witch which has which witches wrist watch'
print(len(s)) #41
comp = zlib.compress(s)
print(len(comp)) #37
decompress = zlib.decompress(comp)
print(decompress)

b__timeit = timeit.Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.031498985015955244
print(b__timeit)
a_b__timeit = timeit.Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.02853694436078457
print(a_b__timeit)


def average(values):
    """Computes the arithmetic mean of a list of numbers.
    40.0
    """
    print(average([20, 30, 70]))
    return sum(values) / len(values)

testmod = doctest.testmod()
print(testmod)

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

 # Calling from the command line invokes all tests

if __name__ == '__main__':
    unittest.main()