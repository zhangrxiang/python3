import time


def decorator():
    t = time.localtime(time.time())
    # print(t)
    print(str(t.tm_year)+"-"+str(t.tm_mon)+"-"+str(t.tm_mday)+" "+str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec))

print(decorator.__name__)
# decorator()
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log2(func):
    print("func"*10)
    return func
@log2
def p():
    print("Happy New Year")

p()

log2(p())
log2(p)

def log3(text):
    print(text)
    def aaa(func):
       return func
    return aaa

@log3("execute")
def tt():
    pass