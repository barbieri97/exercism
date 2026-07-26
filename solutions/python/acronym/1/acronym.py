""" functions to create a acronym """
def abbreviate(words: str) -> str:
    """ return the acronym of the phrase """
    for item in '-_':
        words = words.replace(item, ' ')
    return ''.join([item[0].capitalize() for item in words.split()])
