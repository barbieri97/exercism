""" some functions to count and calculate results for the class. """

def round_scores(student_scores: list) -> list:
    """"Round all provided student scores.

    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    rounded_student_scores = []
    for i in student_scores:
        rounded_student_scores.append(round(i))
    return rounded_student_scores


def count_failed_students(student_scores: list) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    failed_students = 0
    for i in student_scores:
        if i <= 40:
            failed_students += 1
    return failed_students

def above_threshold(student_scores: list, threshold: float):
    """Determine how many of the provided student scores were 'the best'
    based on the provided threshold.

    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    return [i for i in student_scores if i >= threshold]


def letter_grades(highest: int) -> list:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    lower_letter_grades = []
    pattern = (highest - 40) / 4
    for i in range(4):
        highest -= pattern
        lower_letter_grades.append(int(highest + 1))
    return lower_letter_grades[::-1]


def student_ranking(student_scores: list, student_names: list) -> list:
    """Organize the student's rank, name, and grade information in ascending order.

     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    ranking_w_names = []
    for i, (j, k) in enumerate(zip(student_scores, student_names), start=1):
        ranking_w_names.append(f'{i}. {k}: {j}')
    return ranking_w_names
range()


def perfect_score(student_info: list) -> list:
    """Create a list that contains the name and grade of the first student
    to make a perfect score on the exam.

    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for i in student_info:
        if i[1] == 100:
            return i
    return []
