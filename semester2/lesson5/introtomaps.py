# Maps are keyt value pair of objects
my_list = [1,4,7,5]
my_dictionary = {'apples': 2, 'bananas': 5}
print(my_dictionary['apples'])

# put
my_dictionary['bananas'] = 7
my_dictionary['oranges'] = 3
my_dictionary.update({'tomatoes': 3})
# get
my_dictionary['apples']
print(my_dictionary.get('apples'))
print(my_dictionary.get('grapes',0))
print(my_dictionary)

foods_list = ['apples', 'oranges', 'pears']

food_dict = {x:0 for x in foods_list}
print(food_dict)