# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/11
# Time: 22:44
# File: 
# Project: python3
# Location: Wuxi

for year in range(2017):
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
           else:
               # print("{0} 不是闰年".format(year))
               pass
       else:
           print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
    else:
       # print("{0} 不是闰年".format(year))
        pass
