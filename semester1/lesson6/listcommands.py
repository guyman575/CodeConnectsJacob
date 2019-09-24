# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# insert 3 5
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list. print that item
# reverse: Reverse the list.
# quit: stop taking commands
my_list = []
while True:
    command = input("What do you want to do to the list.")
    args = command.split()
    print(args)
    if args[0] == "insert":
        my_list.insert(int(args[1]),int(args[2]))
    elif args[0] == "remove":
        my_list.remove(int(args[1]))
    elif args[0] == "append":
        my_list.append(int(args[1]))
    elif args[0] == "sort":
        my_list.sort()
    elif args[0] == "pop":
        print(my_list.pop())
    elif args[0] == "reverse":
        my_list.reverse()
    elif args[0] == "quit":
        break
    elif args[0] == "print":
        print(my_list)
        

    