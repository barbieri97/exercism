""" functions to help output the lyrics to 'The Twelve Days of Christmas'. """

ORDINAL_AND_GIFITS = {
    1: ('first', 'and a Partridge in a Pear Tree.'),
    2: ('second', 'two Turtle Doves'),
    3: ('third', 'three French Hens'),
    4: ('fourth', 'four Calling Birds'),
    5: ('fifth', 'five Gold Rings'),
    6: ('sixth', 'six Geese-a-Laying'),
    7: ('seventh', 'seven Swans-a-Swimming'),
    8: ('eighth', 'eight Maids-a-Milking'),
    9: ('ninth', 'nine Ladies Dancing'),
    10: ('tenth', 'ten Lords-a-Leaping'),
    11: ('eleventh', 'eleven Pipers Piping'),
    12: ('twelfth', 'twelve Drummers Drumming')
    }
def recite(start_verse, end_verse):
    """ return the song 'The Twelve Days of Christmas' with
    start = start_verse and end = end_verse """
    return [concatenate_string(item) for item in range(start_verse, end_verse + 1)]

def get_ordinal_and_gift(verse: int) -> tuple:
    """
    :param verse: int - number of verse
    :return: tuple -  the cardinal and the gift of the verse
    """
    return ORDINAL_AND_GIFITS.get(verse)

def first_string(verse: int) -> str:
    """
    :param verse: int - number of The Twelve Days of Christmas verse
    :return: str - first part of the string
    """
    return f"On the {get_ordinal_and_gift(verse)[0]} day of Christmas my true love gave to me: "

def second_string(end: int,) -> str:
    """ return the second part of the verse given their number """
    if end == 1:
        return 'a Partridge in a Pear Tree.'
    return ', '.join(get_ordinal_and_gift(item)[1] for item in range(end, 0, -1))

def concatenate_string(verse: int) -> str:
    """ return a concatenate string from first_string and second_string givem a number of verse """
    return first_string(verse) + second_string(verse)
