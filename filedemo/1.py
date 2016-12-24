try:
    f = open('test1.txt', 'r')#只读模式打开test.txt文件
    print(f.read())#读取文件的所有内容
    f.close()#关闭文件
except:
    print(IOError)
    print("no this file")
finally:
    print("finally")


with open('./test.txt', 'r') as f:
    print(f.read())


# with input("input") as l:
#     print(l)


# 读取方法详解
# read():读取文件的所有内容。针对小文件
# read(size):按指定大小来读取文件的内容。size字节大小。针对大文件
# readlines():按行来读取文件的所有内容，返回为list格式。针对配制文件
# 读取模式
# 'r'：读文件
# 'rb'：二进制读文件
# 'w'：写文件
# 'wb'：二进制写文件

