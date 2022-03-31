""" code to isbn verifier exercise """

def is_valid(isbn: str) -> bool:
    """
    :param isbn: str - isbn code to verify
    :return: bool - return True if is a valid isbn code else False
    """
    isbn = isbn.replace('-', '')
    if  len(isbn) != 10 or not isbn[:-1].isdigit() or isbn[-1] not in 'X1234567890':
        return False
    str_2_int = lambda s: int(s) if s != 'X' else 10
    total = sum(str_2_int(isbn[index]) * item for index, item in enumerate(range(10, 0, -1)))
    return total % 11 == 0