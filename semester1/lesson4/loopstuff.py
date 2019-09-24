
# condition = True
# while condition:
#     # Do something
#     print("Hello")
#     condition = False
#     pass
# print("Done")

my_list = ["foo", "bar", "baz", "biz"]
# my_list[0]

length = len(my_list)
number = 0
while number < length:
    print(my_list[number])
    number = number + 1 # number += 1
print("Done")

# for i in range(4,100,5):
#     print(i)

for i in range(length):
    print(my_list[i])


# for i in [0,1,2,3]:
#     print(i)

for element in my_list:
    element = element + "!"
    print(element)

i = 0
while i < len(my_list):
    element = my_list[i]
    print(element)
    i += 1