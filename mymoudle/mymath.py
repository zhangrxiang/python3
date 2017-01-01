def myabs(a):
    if a < 0:
        return -a
    return a


def mysum(*args):
    s = 0
    for i in args:
        s = s + i
    return s