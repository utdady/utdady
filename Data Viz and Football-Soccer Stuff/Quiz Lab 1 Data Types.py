'''
Prompt: Complete and submit the code that creates a Complex number in such a way
        that it can work with the driver program shown below. You need to use
        magic methods that allow the user to add, subtract, multiply,divide, and
        check equality of objects.
'''
# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Complex(%s, %s)' % (self.real, self.imag)    

    # For call to str(). Prints readable form
    def __str__(self):
        return '%s + %si' % (self.real, self.imag)

    # For adding two complex nums.
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # For subtracting two complex nums.
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # For multiplying two complex nums.
    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag), (self.real * other.imag) + (self.imag * other.real))

    # For dividing two complex nums.
    def __truediv__(self, other):
        conjugate = Complex(other.real, (-1) * other.imag)
        numerator = Complex((self.real * conjugate.real) - (self.imag * conjugate.imag), (self.real * conjugate.imag) + (self.imag * conjugate.real))
        denominator = Complex((other.real * conjugate.real) - (other.imag * conjugate.imag), (other.real * conjugate.imag) + (other.imag * conjugate.real))
        return Complex(numerator.real / denominator.real, numerator.imag / denominator.real)

    # To check if two complex nums are equal.
    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False
