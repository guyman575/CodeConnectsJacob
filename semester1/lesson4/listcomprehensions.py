
def only_odd(input_list):
    new_list = []
    for i in range(len(input_list)):
        if(input_list[i] % 2 == 1):
            new_list.append(input_list[i])
    return new_list

def only_odd2(input_list):
    return ["ODD" if x % 2 == 1 else "EVEN" for x in input_list]



# {x: y for x in some_list for y in someotherlist}
my_list = [7,6,5,9,0,1,3,2,5,8]
new_list = only_odd(my_list)
print(new_list)

print(only_odd2(my_list))


