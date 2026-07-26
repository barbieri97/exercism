""" code to exercise prime facotrs """

def factors(value: int) -> list:
    """
    :param value: int - number to verify
    :return: list - list of the prime facotrs
    """
    # if value <= 1:
    #     return []
    prime_factors = []
    factor = 2
    while value > 1:
        if value % factor == 0:
            value /= factor
            prime_factors.append(factor)
            continue
        factor += 1
    return prime_factors
