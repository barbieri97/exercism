""" code to plindrome products exercise """


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError('min must be <= max')
    factors = range(min_factor, max_factor + 1)
    # Esse range vai invertido para se alcançar o maior mais rapido algo como list[::-1]
    products = range(max_factor ** 2, (min_factor**2) -1, -1)
    return get_palindrome(factors, products)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError('min must be <= max')
    factors = range(min_factor, max_factor + 1)
    products = range(min_factor ** 2, (max_factor**2) +1)
    return get_palindrome(factors, products)

def get_palindrome(factors, products):
    """ 
    :param factors: range() - range of factors allowed 
    :param products: range() - range of products allowed
    :return: tuple(int, list) - return the first palindrome and theirs factors
     """
    for product in products:
        if is_palindrome(product):
            pairs = []
            for factor in factors:
                inteiro, resto = divmod(product, factor)
                if resto == 0 and inteiro in factors:
                    pairs.append([factor, inteiro])
            # como o range ja vem ordenado podemos parar no primeiro que encontrarmos
            if len(pairs) > 0:
                return (product, pairs)
    return (None, [])

            


def is_palindrome(number):
    """
    :param numer: int - number to verify if is a palindrome
    :return: bool - return True if is a palindrome, else False
    """
    string = str(number)
    return string == string[::-1]
