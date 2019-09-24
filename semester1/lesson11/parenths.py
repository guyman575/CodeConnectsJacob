from stack import Stack
# {{[[(())]]}

# {[(])}
# {[(
# ]
# ())
def is_matched(expression):
    matches = {'}':'{', ']':'[', ')':'('}
    my_stack = Stack()
    for item in expression:
        if item in matches:
            if matches[item] != my_stack.pop():
                return False
        else:
            my_stack.push(item)
    
    return my_stack.is_empty()