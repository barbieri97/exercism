""" code to saddle ponint exercise """

def saddle_points(matrix):
    """
    :param matrix: list of lists - matrix to find the saddle's points
    :return: list of dicts [{'row': r, 'colum': c}]"""
    if not matrix:
        return []
    if not is_irregular(matrix):
        raise ValueError('irregular matrix')

    points = []
    list_of_colums = create_colums(matrix)
    for index_row, item in enumerate(matrix):
        indexs = get_indexs_maxs_numbers(item)
        for index_colum, number in indexs:
            if number <= min(list_of_colums[index_colum]):
                points.append((index_row + 1, index_colum + 1))
    return [{'row':row, 'column':colum} for row, colum in points]

def create_colums(matrix: list) -> list:
    """
    :param matrix: list of list - matrix to create columns
    :return: list of list - inverse matrix, to access more easily the colums
    """
    new_matrix = [[] for item in range(len(matrix[0]))]
    for row in matrix:
        for index, item in enumerate(row):
            new_matrix[index].append(item)
    return new_matrix

def is_irregular(matrix: list) -> bool:
    """
    :param matrix: list of list - matrix to verify if is regular
    :return: boll - True if matrix is regular else False
    """
    for item in matrix:
        if len(matrix[0]) != len(item):
            return False
    return True

def get_indexs_maxs_numbers(row: list) -> list:
    """
    :param row: list - list to verify the majors items
    :return: list of tuples - return a list with the index and the value of the majors item
    """
    return [item for item in enumerate(row) if item[1] == max(row)]
