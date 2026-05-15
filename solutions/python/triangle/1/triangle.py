def is_triangle(sides):
    sides = sorted(sides)
    return (sides[0] > 0) and ((sides[0] + sides[1]) > sides[2])


def equilateral(sides):
    if not is_triangle(sides):
        return False
    sides = sorted(sides)
    return sides[0] == sides[-1]


def isosceles(sides):
    if not is_triangle(sides):
        return False
    sides = sorted(sides)
    return ((sides[0] == sides[1]) or (sides[1] == sides[2]))


def scalene(sides):
    if not is_triangle(sides):
        return False
    return not equilateral(sides) and not isosceles(sides)
