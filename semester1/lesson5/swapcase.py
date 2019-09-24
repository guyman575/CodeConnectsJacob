# write a function that takes in a string, and reverses the capitalization

# do it however you want
def swap_case_1(string_in):
    new_message = ""
    for letter in string_in:
        if letter.islower():
            new_message += letter.upper()
        else:
            new_message += letter.lower()                       
    return new_message

# make a list comprehension
def swap_case_2(string_in):
    return "".join([letter.upper() if letter.islower() else letter.lower() for letter in string_in])



if __name__ == '__main__':
    #here
    test = "1"
    print(test.isupper())

    assert swap_case_1("Hello World") == "hELLO wORLD"
    print("passed test 1.1")

    assert swap_case_1("My name is Guy. I am a Software Engineer") == "mY NAME IS gUY. i AM A sOFTWARE eNGINEER"
    print("passed test 1.2")

    assert swap_case_1("FoObARBIZbaz") == "fOoBarbizBAZ"
    print("passed test 1.3")

    assert swap_case_2("Hello World") == "hELLO wORLD"
    print("passed test 2.1")

    assert swap_case_2("My name is Guy. I am a Software Engineer") == "mY NAME IS gUY. i AM A sOFTWARE eNGINEER"
    print("passed test 2.2")

    assert swap_case_2("FoObARBIZbaz") == "fOoBarbizBAZ"
    print("passed test 2.3")
    
    
