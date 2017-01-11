# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/11
# Time: 22:43
# File: 
# Project: python3
# Location: Wuxi


# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数

for num in range(100):
    if (num % 2) == 0:
       print("{0} 是偶数".format(num))
    else:
        print("{0} 是奇数".format(num))
