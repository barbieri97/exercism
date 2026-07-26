""" Output the lyrics to 'The Twelve Days of Christmas'. """

def recite(start_verse, end_verse):
    """
    :param start_verse: int - number of The Twelve Days of Christmas verse
    :param end_verse: int - number of The Twelve Days of Christmas verse
    :return: str - verses between start_verse and end_verse
    """
    dic = {1: ['first', 'a Partridge in a Pear Tree'],
    2: ['second', 'two Turtle Doves'],
    3: ['third', 'three French Hens'],
    4: ['fourth', 'four Calling Birds'],
    5: ['fifth', 'five Gold Rings'],
    6: ['sixth', 'six Geese-a-Laying'],
    7: ['seventh', 'seven Swans-a-Swimming'],
    8: ['eighth', 'eight Maids-a-Milking'],
    9: ['ninth', 'nine Ladies Dancing'],
    10: ['tenth', 'ten Lords-a-Leaping'],
    11: ['eleventh', 'eleven Pipers Piping'],
    12: ['twelfth', 'twelve Drummers Drumming']
    }
    if end_verse == start_verse:
        start_verse += 1
        return f'On the {dic[end_verse][0]} day of Christmas my true love gave to me: {dic[end_verse][1]}'
    return recite(start_verse, end_verse -1)

if __name__ == '__main__':
    print(recite(1, 12))
