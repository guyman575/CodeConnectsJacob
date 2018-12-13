def median(my_list):
    new_list = sorted(my_list)
    if len(new_list) % 2:
        return new_list[len(new_list)//2]
    else:
        return (new_list[len(new_list)//2 - 1] + new_list[len(new_list)//2])/2


def max_num(my_list):
    return max(my_list)

EXAMPLE_STRING = "Hello World"

# # [0,2,5,5,6,7,9,9]
# list_a = [9,5,5,0,2,6,9,7]
# print(median(list_a))
# print(list_a)