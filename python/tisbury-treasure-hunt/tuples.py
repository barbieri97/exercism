""" a small program (a set of functions, really) to better organize their hunt information. """

from re import sub

def get_coordinate(record: tuple) -> str:
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[-1]


def convert_coordinate(coordinate: str) -> tuple:
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """
    return tuple(item for item in coordinate)


def compare_records(azara_record: tuple, rui_record: tuple) -> bool:
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    return convert_coordinate(azara_record[-1]) == rui_record[1]


def create_record(azara_record: tuple, rui_record: tuple) -> tuple:
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return 'not a match'


def clean_up(combined_record_group: tuple) -> str:
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned".
    Excess coordinates and information removed.
    """
    string = ''
    for item in combined_record_group:
        string += str(item) + '\n'
    return sub(r' \'[0-9][A-Z]\',', '', string)
