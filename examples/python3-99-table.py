# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/11
# Time: 22:52
# File: 
# Project: python3
# Location: Wuxi



# 九九乘法表
for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()
