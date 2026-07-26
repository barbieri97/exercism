""" this modulo create a table of the tournament """

def tally(rows: list) -> list:
    """ receive the matchs and return a table """
    header = [f"{'Team': <31}|{'MP': ^4}|{'W ': >4}|{'D ': >4}|{'L ': >4}|{'P': >3}"]
    list_of_results = create_list_results(rows)
    dict_of_results = create_dict_of_results(list_of_results)
    table = create_table(dict_of_results)
    return header + table


def compute_match(row: str):
    """ recive a string with the result and return a list with the each club points """
    club_1, club_2, result = row.split(';')
    if result == 'win':
        return (club_1, [1, 1, 0, 0, 3]), (club_2, [1, 0, 0, 1, 0])
    if result == 'loss':
        return (club_1, [1, 0, 0, 1, 0]), (club_2, [1, 1, 0, 0, 3])
    if result == 'draw':
        return (club_1, [1, 0, 1, 0, 1]), (club_2, [1, 0, 1, 0, 1])
    return None

def create_list_results(rows: list):
    """ create a list with all matches results """
    results = []
    for item in rows:
        club_1, club_2 = compute_match(item)
        results.append(club_1)
        results.append(club_2)
    return results

def create_dict_of_results(results: list) -> dict:
    """ with a list of results create a dictionary to compute the results """
    table = {}
    for club, statics in results:
        if club in table:
            for index in range(5):
                table[club][index] += statics[index]
        else:
            table[club] = statics
    return table

def create_table(table: dict) -> list:
    """ create a list of string that implement the table """
    list_2_sort = lambda table: [[item[0], item[1][4]] for item in list(table.items())]
    clubs = list_2_sort(table)
    sorted_clubs = sort_list(clubs)
    table_list = []
    for item in sorted_clubs:
        played, win, draw, lost, points = table[item]
        table_list.append(
            f"{item: <31}|{played: >3} |{win: >3} |{draw: >3} |{lost: >3} |{points: >3}"
            )
    return table_list

def sort_list(table_list: list) -> list:
    """ sort the clubs with the points """
    work_list = table_list[:]
    for index, item in enumerate(work_list):
        current_element = item
        while index > 0 and work_list[index - 1][1] < current_element[1]:
            work_list[index] = work_list[index - 1]
            index -= 1
        work_list[index] = current_element
    for index, item in enumerate(work_list):
        if work_list[index][1]==work_list[index-1][1] and work_list[index][0]<work_list[index-1][0]:
            work_list[index], work_list[index - 1] = work_list[index - 1], work_list[index]
    return [item[0] for item in work_list]
