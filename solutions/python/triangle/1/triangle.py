""" code to triagle exercise """

def equilateral(sides: list) -> bool:
    """
    :param sides: list - sides of triagle
    :return: bool - True if is equilateral
    """
    side_a,side_b,side_c = sides
    if side_a == side_b == side_c and check_triangle(sides):
        return True
    return False

def isosceles(sides: list) -> bool:
    """
    :param sides: list - sides of triagle
    :return: bool - True if is equilateral
    """
    side_a,side_b,side_c = sides
    if (side_a == side_b or side_b == side_c or side_c  == side_a) and check_triangle(sides):
        return True
    return False



def scalene(sides: list) -> bool:
    """
    :param sides: list - sides of triagle
    :return: bool - True if is equilateral
    """
    side_a,side_b,side_c = sides
    if (side_a != side_b and side_b != side_c and side_c != side_a) and check_triangle(sides):
        return True
    return False

def degenerate(sides: list) -> bool:
    """
    :param sides: list - sides of triagle
    :return: bool - True if the sum of 2 sides are equal
    than third
    """
    if not check_triangle(sides):
        return False
    for index, item in enumerate(sides):
        if item == sides[index -1] + sides[index - 2]:
            return True
    return False


def check_triangle(sides: list) -> bool:
    """
    :param sides: list - sides of triagle
    :return: bool - True if the sides are greater than 0 and the sum of 2 sides are greater
    than third
    """
    for item in sides:
        if item <= 0:
            return False
    for index, item in enumerate(sides):
        if item > sides[index - 1] + sides[index - 2]:
            return False
    return True
