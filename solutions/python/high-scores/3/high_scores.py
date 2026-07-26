""" Your task is to write methods that return the highest score from the list, the last added """

class HighScores:

    def __init__(self, scores: list):
        self.scores = scores

    def latest(self) -> int:
        """
        :param scores: list - list of scores(int) of a game
        :return: int - the latest score of the game
        """
        return self.scores[-1]


    def personal_best(self) -> int:
        """
        :param scores: list - list of scores(int) of a game
        :return: int - the highest score of the game
        """
        return max(self.scores)


    def personal_top_three(self) -> list:
        """
        :param scores: list - list of scores(int) of a game
        :return: list - the three highest score of the game
        """
        sorted_list = self.scores[:]
        sorted_list.sort()
        return sorted_list[-1:-4:-1]
