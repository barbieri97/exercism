"""Given a string representing a matrix of numbers, return the rows and columns of that matrix."""

class Matrix:
    """ this class create a matrix with a string  """

    def __init__(self, matrix_string: str):
        self.matrix = []
        for item in matrix_string.splitlines():
            lines = []
            for colum in item.split():
                lines.append(int(colum))
            self.matrix.append(lines)

    def row(self, index: int) -> list:
        """
        :param index: int - index of a matrix's line
        :return: list - list of line numbers of matrix
        """
        return self.matrix[index - 1]

    def column(self, index: int) -> list:
        """
        :param index: int - index of a matrix's colum
        :return: list - list of line numbers of matrix
        """
        return [self.matrix[linha][index - 1] for linha in range(len(self.matrix))]
