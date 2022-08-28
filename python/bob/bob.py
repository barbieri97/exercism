""" code to bob exercise """

def response(hey_bob: str) -> str:
    """
    :param hey_bob: str - phrase to bob
    :return: str - bob response
    """

    if hey_bob.isspace() or not hey_bob:
        return 'Fine. Be that way!'
    hey_bob = hey_bob.strip()
    if hey_bob.endswith('?'):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return 'Sure.'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
        