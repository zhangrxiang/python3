def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


def fact2(n):
    if n==1:
        return 1
    return n + fact(n - 1)



print(fact(5))
print(fact2(5))


def fact3(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)



print(fact_iter(1,2))
print(fact_iter(2,2))
print(fact_iter(3,2))
print(fact_iter(4,2))
print(fact_iter(5,2))