# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/10
# Time: 22:25
# File: 
# Project: python3
# Location: Wuxi


# 用户输入摄氏温度

# 接收用户收入
celsius = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))
