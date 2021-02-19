from unittest import TestCase


class Point:

    def __init__(self, x, y, a, b):
        self.a = a;
        self.b = b;
        self.x = x;
        self.y = y;
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x,y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
        and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format
                            (self, other))

        if self.x is None:  # <3>
            return other
        if other.x is None:  # <4>
            return self
            # end::source3[]

            # Case 1: self.x == other.x, self.y != other.y
            # Result is point at infinity
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

            # Case 2: self.x ≠ other.x
            # Formula (x3,y3)==(x1,y1)+(x2,y2)
            # s=(y2-y1)/(x2-x1)
            # x3=s**2-x1-x2
            # y3=s*(x1-x3)-y1
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s ** 2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

            # Case 3: self == other
            # Formula (x3,y3)=(x1,y1)+(x1,y1)
            # s=(3*x1**2+a)/(2*y1)
            # x3=s**2-2*x1
            # y3=s*(x1-x3)-y1
        if self == other:
            s = (3 * self.x ** 2 + self.a) / (2 * self.y)
            x = s ** 2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

            # Last case: self == other and the y coordinate is 0
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

    def __rmul__(self, coefficient):
        coef = cofficeint
        current = self 
        result = self.__class__(None, None, self.a, self.b)


        return result


# p1 = Point(-1, -1, 5, 7)
# p2 = Point(-1, 1, 5, 8)
# p1.__ne__(p2)

class PointTest(TestCase):
    def test_ne(self):
        a = Point(x=3, y=-7, a=5, b=7)
        b = Point(x=18, y=77, a=5, b=7)
        self.assertTrue(a != b)
        self.assertFalse(a != a)

    def test_add0(self):
        a = Point(x=None, y=None, a=5, b=7)
        b = Point(x=2, y=5, a=5, b=7)
        c = Point(x=2, y=-5, a=5, b=7)
        self.assertEqual(a + b, b)
        self.assertEqual(b + a, b)
        self.assertEqual(b + c, a)

    def test_add1(self):
        a = Point(x=3, y=7, a=5, b=7)
        b = Point(x=-1, y=-1, a=5, b=7)
        self.assertEqual(a + b, Point(x=2, y=-5, a=5, b=7))

    def test_add2(self):
        a = Point(x=-1, y=-1, a=5, b=7)
        self.assertEqual(a + a, Point(x=18, y=77, a=5, b=7))
