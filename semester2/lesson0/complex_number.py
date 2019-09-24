import math

# 5 + 7i
class Complex():

    def __init__(self,real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, value): # +
        return Complex(self.real + value.real, self.imaginary + value.imaginary)

    def __sub__(self, value): # - 
        return Complex(self.real - value.real, self.imaginary - value.imaginary)

    # real = real1*real2 - imaginary1*imaginary2
    # imaginary = real1*imaginary2 + real2*imaginary1
    def __mul__(self, value): #  *
        return Complex(self.real * value.real - self.imaginary * value.imaginary,
        self.real * value.imaginary + value.real * self.imaginary)
        

    def __truediv__(self, value): # /
        pass

    def __floordiv__(self, value): # //
        pass

    def __mod__(self, value): # %
        pass

    def __str__(self):
        return str(self.real) + "+" + str(self.imaginary) + "i"
        


def main():
    complex1 = Complex(1,1)
    complex2 = Complex(2,2)
    print(complex1 - complex2)
    print(complex1 + complex2)
    print(complex2 * complex2 + complex1)
    

if __name__ == "__main__":
    main()