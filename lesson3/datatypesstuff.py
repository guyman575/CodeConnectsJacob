# # Dict (Dictionary)
my_dict = {"one" : 1, "two": 2, "three": 3}
if("four" in my_dict):
    print(my_dict["four"])
else:
    my_dict["four"] = 4
print(my_dict.get("four"))

my_dict["one"] = 100
print(my_dict)
my_other_dict = dict() #{}



# Set
my_set = set(["one","two","three"])
print("one" in my_set)
my_set.add("four")
my_set.remove("one")
a_random_item = my_set.pop()
print(my_set, a_random_item)
# List
my_list = [9,3,4,2,6,4]
print(my_list[0])
list_length = len(my_list)
print(list_length)
print(my_list[list_length - 1])
my_list.append(7)
my_list.insert(1,100)
my_list.remove(2)
print(my_list)
# Tuple
my_tuple = tuple([1,2,3]) # (1,2,3)
