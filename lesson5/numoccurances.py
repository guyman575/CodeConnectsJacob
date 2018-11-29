# write a function that returns the number of occurances of each element in a list

# Only use loops and arithmatic (and data structures)
def num_occurances_1(list_in):
    num_counts = {}
    for number in list_in:
        if number in num_counts:
            num_counts[number] += 1
        else:
            num_counts[number] = 1 
    return num_counts

# Are there any list methods that could help?
def num_occurances_2(list_in):
    num_counts = {}
    for number in list_in:
        if number not in num_counts:
            num_counts[number] = list_in.count(number)
    return num_counts

# What about a dictionary comprehension?
def num_occurances_3(list_in):
    return {k: list_in.count(k) for k in list_in}

def num_occurances_4(list_in):
    num_counts = {}
    no_duplicates = set(list_in)
    for number in no_duplicates:
        num_counts[number] = list_in.count(number)
    return num_counts


if __name__ == '__main__':
    print(set([1,1,1,1,1,1]))
    assert num_occurances_1([1,3,5,7,1,1,6,3,9,7,8]) == {1: 3, 3: 2, 5: 1, 7: 2, 6: 1, 9: 1, 8: 1}
    print("passed")
    assert num_occurances_2([1,3,5,7,1,1,6,3,9,7,8]) == {1: 3, 3: 2, 5: 1, 7: 2, 6: 1, 9: 1, 8: 1}
    print("passed")
    assert num_occurances_3([1,3,5,7,1,1,6,3,9,7,8]) == {1: 3, 3: 2, 5: 1, 7: 2, 6: 1, 9: 1, 8: 1}
    print("passed")
    assert num_occurances_4([1,3,5,7,1,1,6,3,9,7,8]) == {1: 3, 3: 2, 5: 1, 7: 2, 6: 1, 9: 1, 8: 1}
    print("passed")
    