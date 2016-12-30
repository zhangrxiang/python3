def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

fab(10)

def fab2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L
print(fab2(10))

class Fab():

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


mygenerator = (x*x for x in range(3))
mygenerator2 = [x*x for x in range(3)]

print(type(mygenerator))
print(type(mygenerator2))

gg = ()
print(type(gg))
gg2 = (1,)
print(type(gg2))
gg3 = range(10)
print(type(gg3))
gg4 = (range(10))
print(type(gg4))


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

gg5 = createGenerator()
print(type(gg5))
print(next(gg5))
print(next(gg5))
print(next(gg5))

print("*"*50)
def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for i in fab3(5):
    print(i)



def mysum(n):
    sum = 0
    while(0 < n):
        sum = sum + n
        yield sum
        n = n - 1

print("$"*50)
for i in mysum(10):
    print(i)


def mysum2(n):
    sum = 0
    L = []
    while(0 < n):
        sum = sum + n
        L.append(sum)
        n = n - 1
        yield L

s = mysum2(10)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))