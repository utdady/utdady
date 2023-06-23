from math import sqrt

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def __add__(self, point):
        return Point2D(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point2D(self.x - point.x, self.y - point.y)

    def __mul__(self, scalar):
        return Point2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

if __name__ == '__main__':
    A = Point2D(1, 1)
    B = Point2D(0, 0)
    C = Point2D(0, 3)
    D = Point2D(0, 1)
    print(A)             # should print (1.0, 1.0)
    print(A + B)         # should print (1.0, 1.0)
    print(A - C)         # should print (1.0, -2.0)
    print(A * 3)         # should print (3.0, 3.0)
    print(D.distance(C)) # should print 2.0 
    print(B == A)        # should print False
    print(B == A * 0)    # should print True  
    print(distance(A,B))
