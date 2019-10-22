from math import sqrt

my_nums = [77, 8, -4, 5, 0, 107, 3, 42, -6, 7 ,88, 177, 4, -33]
# [thing_to_include for thing_to_include in things if CONDITION]
my_nums_odd = [num for num in my_nums if num % 2 == 1] # get odd numbers in my_nums

print(my_nums_odd)

my_nums_positive = [num for num in my_nums if num > 0]

print(my_nums_positive)

my_nums_negative = [num for num in my_nums if num < 0]

print(my_nums_negative)

my_nums_squared = [num**2 for num in my_nums if num > 0]
print(my_nums_squared)

my_nums_sqrt_even = [sqrt(num) if num > 0 else num for num in my_nums if num % 2 == 0]
print(my_nums_sqrt_even)