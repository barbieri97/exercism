""" Your task is to convert a number into a string that contains raindrop sounds corresponding
to certain potential factors """


def convert(number: int) -> str:
    """
    :param number: int - Number to check his factor
    :return: str - string if the 'sound' of a drop (pling, plang, plong), that can be concatenate
    """
    drop_sound = ''
    for num, sound in zip((3, 5, 7), ('Pling', 'Plang', 'Plong')):
        if number % num == 0:
            drop_sound += sound
    return drop_sound if drop_sound != '' else str(number)
