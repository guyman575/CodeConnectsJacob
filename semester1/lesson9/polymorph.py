print(1 + 2)
print("Hello " + "world")
print([1,2,3] + [4,5,6])
# NOT ALLOWED
# def my_func(num):
#     print(num)
# def my_func(num1, num2):
#     print(num1 + num2)
# my_func(1)
# my_func(2,3)

class MyNumber():

    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return MyNumber(self.value + other.value)
    

    
one = MyNumber(1)
two = MyNumber(2)
three = one + two
print(three.value)

# OPERATOR	FUNCTION	            METHOD DESCRIPTION
# + 	    __add__(self, other) 	 Addition
# * 	    __mul__(self, other) 	 Multiplication
# - 	    __sub__(self, other) 	 Subtraction
# % 	    __mod__(self, other) 	 Remainder
# / 	    __truediv__(self, other) 	 Division
# < 	    __lt__(self, other) 	 Less than
# <= 	    __le__(self, other) 	 Less than or equal to
# == 	    __eq__(self, other) 	 Equal to
# != 	    __ne__(self, other) 	 Not equal to
# > 	    __gt__(self, other) 	Greater than
# >= 	    __ge__(self, other) 	 Greater than or equal to
# [index] 	__getitem__(self, index) 	 Index operator
# in 	    __contains__(self, value) 	Check membership
# len 	    __len__(self) 	                The number of elements
# str 	    __str__(self) 	            The string representation