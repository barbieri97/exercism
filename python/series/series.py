""" code to series exercise """


def slices(series, length):
    """
    Return the substrings in a string

    :param series: str - string to get the substrings
    :param length: int - length of the substrings
    :return: list - list of the substrings
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if series == '':
        raise ValueError('series cannot be empty')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')

    numbers_of_substrings = (len(series) - length) + 1
    return [series[i:i+length] for i in range(numbers_of_substrings)]
