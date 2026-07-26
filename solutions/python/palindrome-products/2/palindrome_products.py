""" code to plindrome products exercise """


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if max_factor <= min_factor:
        raise ValueError('min must be <= max')

    possible_products = [
                (n1 * n2, tuple(sorted([n1, n2]))) for n1 in range(min_factor, max_factor + 1)
                for n2 in range(min_factor, max_factor + 1)
                ]
    palindromes = [item for item in possible_products if str(item[0]) == str(item[0])[::-1]]
    palindromes.sort()
    large_palindrome = tuple(item for item in palindromes if item[0] == palindromes[-1][0])
    large_palindrome = set(large_palindrome)
    products = [item[1] for item in large_palindrome]
    products.sort()
    palindrome = tuple(large_palindrome)[0][0]

    return palindrome, products


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor <= min_factor:
        raise ValueError('min must be <= max')

    possible_products = [
                (n1 * n2, tuple(sorted([n1, n2]))) for n1 in range(min_factor, max_factor + 1)
                for n2 in range(min_factor, max_factor + 1)
                ]
    palindromes = [item for item in possible_products if str(item[0]) == str(item[0])[::-1]]
    palindromes.sort()
    small_palindrome = tuple(item for item in palindromes if item[0] == palindromes[0][0])
    small_palindrome = set(small_palindrome)
    products = [item[1] for item in small_palindrome]
    products.sort()
    palindrome = tuple(small_palindrome)[0][0]

    return palindrome, products