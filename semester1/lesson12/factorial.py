# 6! = 1*2*3*4*5*6

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(6))

def factorial_iterative(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f