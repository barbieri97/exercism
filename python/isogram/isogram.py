""" identify if a string have repeat caracters """



def is_isogram(string: str) -> bool:
    """
    :param string: str - string to verify if have repeat caracters
    :return: bool - return if the string is a isogram
     """
    string = string.lower()
    for item in string:
        if string.count(item) > 1 and item not in ' -.':
            return False
    return True