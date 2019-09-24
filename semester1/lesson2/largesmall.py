a = 6
b = 7
c = 8
if a == b or a == c or b == c:
    print("Please pick 3 different numbers")
else:
    if a < b and a < c :
        print (a)
    elif b < a and b < c:
        print(b)
    elif c < a and c < b:
        print (c)

    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)