""" solution to perfect-numbers exercise """

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.",)

    sum_proper_divisors = sum((item for item in range(1, number) if number % item == 0))
    if sum_proper_divisors == number:
        return 'perfect'
    if sum_proper_divisors > number:
        return 'abundant'
    if sum_proper_divisors < number:
        return 'deficient'
    return None
