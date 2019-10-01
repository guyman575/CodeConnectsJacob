# in python, and in many other languages,
# a string is just a list or array of characters
hello_string = "hello"
# This can be defined as a literal by typing
# it in single or double quotes
world_string = 'world'

# we can treat them similarly to arrays in many ways
print(hello_string[1])
print(len(world_string))

# As we have seen before we can concatonate strings
print(hello_string + world_string)
print(hello_string + " " + world_string)

# or we can make the string a template and insert variables
hello_world_string1 = f'{hello_string} {world_string}!'
hello_world_string2 = '%s %s!' % (hello_string, world_string)
print(hello_world_string1, hello_world_string2)

# another thing we can do is multiply strings!
print(hello_string * 5)
# or add spaces. Why doesnt this one work?
print(hello_string +  " " * 5)
# but this one does?
print((hello_string +  " ") * 5)

# strings are immutable. This means whenever we create them,
# they cannot change. When we add two strings together, it
# creates a new one. This is why you can pass a string into
# a function and it doesnt modify it outside the function
def modify_string(my_string):
    my_string = "modified string"

example_string = "example"
modify_string(example_string)
print(example_string)

# my_list = [1,2,3]
# my_list[0] = 2
# print(my_list)
# This also means that unlike arrays and lists, we cannot 
# modify the string using indices
# example_string[0] = 'j'
example_string = "jxample"

