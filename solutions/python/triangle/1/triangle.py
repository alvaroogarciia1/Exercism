def checkTriangleZero(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a > 0 and b > 0 and c > 0

def checkTriangleEq(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    ab = a + b
    bc = b + c
    ac = a + c
    return ab >= c and bc >= a and ac >= b

def checkTriangle(sides):
    return checkTriangleZero(sides) and checkTriangleEq(sides)

def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return checkTriangle(sides) and a == b == c


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return checkTriangle(sides) and ((a == b) or (a == c) or (b == a) or (b == c))


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return checkTriangle(sides) and ((a != b) and (a != c) and (b != a) and (b != c))
