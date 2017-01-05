import os
from datetime import datetime, tzinfo
import time


dt = datetime(2017, 1, 5, 22, 22, 22, 222222) # 用指定日期时间创建datetime
print("dt : ", dt)
print("timestamp : ", dt.timestamp())
print("date : ", dt.date())
print("time : ", dt.time())
print("astimezone : ", dt.astimezone(None))
print("ctime : "+dt.ctime())

# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

# timestamp = datetime.timestamp()
# print("timestamp", timestamp)
# fromtimestamp = datetime.fromtimestamp()
# print("fromtimestamp", fromtimestamp)
now = datetime.now()
print("datetime.now", now)


for i in range(10):
    now = datetime.now()  # 获取当前datetime
    print(now)
    time.sleep(1)

