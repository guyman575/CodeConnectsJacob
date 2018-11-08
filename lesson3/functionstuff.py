
def example(param1,param2):
    print("Adding")
    param1 += 1
    return param1 + param2
one = 1
two = 2

sum_of_nums = example(one,two)
example(4,5)
print(sum_of_nums,one,two)



def sideeffectexample(my_list):
    my_list.append(7)
    # return my_list[len(my_list) -1]

list1 = [1,2,3,4]
print(sideeffectexample(list1))
print(list1)

def maxnumber(num_1,num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

my_result = maxnumber(3,4)
print(my_result)