# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/10
# Time: 22:27
# File: 
# Project: python3
# Location: Wuxi

# 引入 datetime 模块
import datetime


def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# 输出
print(get_yesterday())
