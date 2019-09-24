import math # math.fabs(num)
import random #random.randint(low,high)


def randomSum(numRandoms):
    answer = 0
    for i in range (0, numRandoms + 1):
        num1 = math.fabs(random.randint(-100,100))
        print(num1)
        answer += num1
    return answer


print(randomSum(5))

