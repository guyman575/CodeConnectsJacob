# https://docs.python.org/3/library/stdtypes.html#set
# https://docs.python.org/3/tutorial/datastructures.html#sets

basket_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket_list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(basket_set, basket_list)

print('orange' in basket_set)
# This does work, but its slower
print('orange' in basket_list)

basket_set.add('grapes')
print(basket_set)
basket_set.remove('pear')
print(basket_set)
new_set = set()
new_set2 = set(basket_list)
print(list(new_set2))

basket_set.discard('asdasjkdl')
