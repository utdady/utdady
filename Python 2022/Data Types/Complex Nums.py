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

    def __add__(self, c1, c2):
        self.real = c1.real + c2.real
        self.imag = c1.imag + c2.imag
