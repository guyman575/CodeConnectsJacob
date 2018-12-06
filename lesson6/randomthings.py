# Parsing strings
my_vegetables = "potatoes, tomatoes, onion, cucumber"
veggie_list = my_vegetables.split(", ")
print(veggie_list)
print(", ".join(veggie_list))


# sorting lists
my_list = [3.3,1,7,8,3,5,0,2,2]
my_list.sort()
print(my_list)
string_list = ["1","7","8","3","5","0","2","2"]

print(string_list[::2])
print(string_list[1::2])

print(sorted(string_list))
print("0" < "1")
print(sorted(veggie_list))

def my_function(param1=1, param2=2):
    return param1 + param2

print(my_function())
print(my_function(5,6))
print(my_function(param2=6,param1=0))