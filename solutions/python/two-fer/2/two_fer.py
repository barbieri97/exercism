""" Given a name, return a string with the message:

One for name, one for me.

Where "name" is the given name.

However, if the name is missing, return the string:

One for you, one for me. """

def two_fer(name: str= 'you') -> str:
    """
    :param name: str - name that should be in the string
    :return: str - string with the name if name is givin; else string with 'you' isntead
    """
    return f'One for {name}, one for me.'
