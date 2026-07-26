""" code to differnce of squares exercise """

def square_of_sum(number):
    """
    :param number: int - number of the firsts natural numbers
    :return: int - the square of the sum of firsts n numbers naturals
    """
    return sum(i for i in range(number + 1))**2


def sum_of_squares(number):
    """
    :param number: int - number of the firsts natural numbers
    :return: int - number of sum of the square of the firsts natural numbers
    """
    return sum(i**2 for i in range(number + 1))

def difference_of_squares(number):
    """
    :param number: int - number of the firsts natural numbers
    :return: int - difference of square_of_sum and sum_of_square
    """
    return square_of_sum(number) - sum_of_squares(number)
