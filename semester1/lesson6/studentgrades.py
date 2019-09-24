# read in input from the user. The input can be one of two types

# 1. Data entry
# <Name> <Class1> <Grade1> <Class2> <Grade2> ...
# add the student and his grades to a data structure that
# can be accessed later

# 2. Data access
# <Name> <Class>
# Student <Name> has a grade of <Grade> in <Class>

# 3. quit
my_dict = {}

while True:
    command = input("What do you want to do to your grades?")
    args = command.split()
    if len(args) > 2:
        name = args[0]
        args.pop(0)
        my_dict[name] = {}
        # {k:v for k in args[::2] for v in args[1::2]}
        for i in range(0,len(args),2):
            class_name = args[i]
            grade = args[i + 1]
            my_dict[name][class_name] = int(grade)
    elif len(args) == 2:
        name = args[0]
        class_name = args[1]
        grade = my_dict[name][class_name]
        print(f"Student {name} has a grade of {grade} in {class_name}")
    elif args[0] == "quit":
        break
