# Basics
colors = ['red', 'green' , 'blue' ]
# print the first element
print(colors[0])
# print blue using the list
print(colors[2])
# print the length of the list
print(len(colors))
# add purple to the end
colors.append("purple")
# add orange and yellow where they belong
colors.insert(1, "Orange")
colors.insert(2, "Yellow")
# copy the list
# colors_new = colors will not copy!!!
colors_new = colors.copy()


print(colors_new)
print(colors)
