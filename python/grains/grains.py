""" code to grains exercise """

def square(number: int) -> int:
    """
    :param number: int - a square on the chessboard
    :return: int - number of grains in a given square
    """
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """
    :return: int -  total of grains in the chessboard
    """
    return sum([square(x) for x in range(1, 65)])
