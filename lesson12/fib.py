# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci_iterative(n):
    if n <= 1:
        return n
    prevprev = 0
    prev = 1
    for i in range(0,n-1):
        temp = prevprev
        prevprev = prev
        prev = temp + prev
    return prev


def fibonacci_recursive(n):
    print(n)
    i = input()
    if n <= 1:
        return n
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

fibonacci_recursive(5) # 5 4 3 2 1 0 1 2 1 0 3 2 1 0 1
