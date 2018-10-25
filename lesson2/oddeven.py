# take in a number, print Odd if it is odd,
# Even if it is even
# 7 % 2 == 1, 6 % 2 == 0
number = int(input("Pick a number"))

if number != 0:
    if number < 0:
        print("Your number is to little")
    elif number > 100:
        print("Your number is to big")
    elif number % 2 == 0:
        print("Your number is Even")
    else:
        print("Your number is Odd")
