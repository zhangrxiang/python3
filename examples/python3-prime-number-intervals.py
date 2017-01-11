# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/11
# Time: 22:47
# File: 
# Project: python3
# Location: Wuxi

# 输出指定范围内的素数

for num in range(1, 102):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
