""" Your task is to write methods that return the highest score from the list, the last added """

def latest(scores: list) -> int:
    """
    :param scores: list - list of scores(int) of a game
    :return: int - the latest score of the game
    """
    return scores[-1]


def personal_best(scores: list) -> int:
    """
    :param scores: list - list of scores(int) of a game
    :return: int - the highest score of the game
    """
    scores.sort()
    return scores[-1]


def personal_top_three(scores: list) -> list:
    """
    :param scores: list - list of scores(int) of a game
    :return: list - the three highest score of the game
    """
    scores.sort()
    return scores[-1:-4:-1]
