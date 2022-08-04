# Implements a simple 'vector' class intended to better represent a
# numeric vector, rather than a general tuple.
class vector(tuple):
    '''Numeric vector class.'''
    def __add__(self, other):
        '''Implement vector addition.

        This implementation will allow for either vector + iterable
        or vector + scalar.
        '''
        ls = []
        try:
            for x, y in zip(self, other):
                ls.append(x + y)
        except TypeError: # zip failed, other is scalar.
            for x in self:
                ls.append(x + other)
        return vector(ls)
            
    def __mul__(self,other):
        if len(self) == 3 and type(other) == int:
            return ((self[0] * other) , (self[1] * other) , (self[2] * other))
        elif len(self) == 1 and len(other) == 1:
            return self * other
        elif len(self) == 3 and len(other) == 3:
            return (self[0] * other[0]) + (self[1] * other[1]) + (self[2] * other[2])
        else:
            return None


    def magnitude(self):
        '''Compute the magnitude of a vector.'''
        r = 0
        for x in self:
            r += x * x
        return r ** 0.5

a = vector((1, 2, 5))
b = vector((6, 2, 3))
assert a + b == (7, 4, 8)
assert a + 1 == (2, 3, 6)
assert a + (3, -1, -2) == (4, 1, 3)
assert b.magnitude() == 7.0

#Added tests
assert a * b == 25
assert a * 5 == (5,10,25)


print("Tests passed")

