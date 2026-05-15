def is_triangle(func):
    def inner(sides):    
        sides = sorted(sides)
        return (len(sides) == 3) and (sides[0] > 0) and ((sides[0] + sides[1]) > sides[2]) and func(sides)
    return inner


@is_triangle
def equilateral(sides):
    sides = sorted(sides)
    return sides[0] == sides[-1]


@is_triangle
def isosceles(sides):
    sides = sorted(sides)
    return ((sides[0] == sides[1]) or (sides[1] == sides[2]))


@is_triangle
def scalene(sides):
    return not equilateral(sides) and not isosceles(sides)
