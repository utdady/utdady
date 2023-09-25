# Vector2D class for operating with vector objects.
import math

class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2D((-1) * self.x, (-1) * self.y)

    def __mul__(self, scalar):
        return Vector2D(scalar * self.x, scalar * self.y)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector2D(scalar / self.x, scalar / self.y)
        else:
            return None
        
    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    def __ge__(self, other):
        '''
        selfMAG = pow(pow(self.x, 2) + pow(self.y, 2), 0.5)
        otheMAG = pow(pow(othe.x, 2) + pow(othe.y, 2), 0.5)
        if selfMAG >= otheMAG:
            return True
        else:
            return False
        '''
        if self.magnitude() >= other.magnitude():
            return True
        else:
            return False

    def __lt__(self, other):
        '''
        selfMAG = pow(pow(self.x, 2) + pow(self.y, 2), 0.5)
        otheMAG = pow(pow(othe.x, 2) + pow(othe.y, 2), 0.5)
        if selfMAG < otheMAG:
            return True
        else:
            return False
        '''
        if self.magnitude() < other.magnitude():
            return True
        else:
            return False

    def __hash__(self):
        return id(self)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def magnitudeSquared(self):
        return pow(self.x, 2) + pow(self.y, 2)

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return Vector2D(self.x / mag, self.y / mag)
        return None
    
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def copy(self):
        return Vector2D(self.x, self.y)
