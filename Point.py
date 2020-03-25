class Point:

    def __init__(self, x, y, a, b):
        self.a = a;
        self.b = b;
        self.x = x;
        self.y = y;
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x,y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
        and self.a == other.a and self.b == other.b

p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 8)
