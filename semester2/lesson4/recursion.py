# Factorial
# n! = n * (n-1) * ... * 1
# 5! = 5 * 4 * 3 * 2 * 1

def factorialIterative(num):
    final_num = 1
    for i in range(num):
        final_num = final_num * (num - i)
    return final_num

def factorialIterative2(num):
    final_num = 1
    while(num != 0):
        final_num *= num
        num -= 1
    return final_num

print(factorialIterative(5))
print(factorialIterative2(5))

# factorialRecursive(5)
# -- factorialRecursive(4)
# ---- factorialRecursive(3)
# ------ factorialRecursive(2)
# -------- factorialRecursive(1)
# ---------- factorialRecursive(0)
def factorialRecursive(num):
    if num == 0:
        return 1
    return num * factorialRecursive(num - 1)
    

print(factorialRecursive(5))

# 0 1 1 2 3 5 8 13 21 34
# result of adding previous two numbers together
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))

# print(fibonacci(50))

