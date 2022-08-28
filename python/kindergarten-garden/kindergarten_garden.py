""" classes to help the organization of the garden class """

NAME_OF_PLANTS = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets'
}

def separete_plants_in_subgroups(diagram: list) -> list:
    """ divide the items of a list in subgroups of two items """
    group_plants = []
    while len(diagram) > 0:
        first_item = diagram.pop(0)
        second_item = diagram.pop(0)
        group_plants.append([first_item, second_item])
    return group_plants

def convert_initial_4_name(diagram: list) -> list:
    """ return a list with the name of the plants, instead their initials """
    for index, item in enumerate(diagram):
        diagram[index] = NAME_OF_PLANTS.get(item)
    return diagram

class Garden:
    """ organization for garden class """
    def __init__(self, diagram: str, students=('Alice', 'Bob', 'Charlie', 'David','Eve', 'Fred',
                                        'Ginny','Harriet','Ileana', 'Joseph', 'Kincaid', 'Larry')):
        """ constructor """
        self.first_row, self.second_row= tuple(diagram.splitlines())
        self.students: list = list(students)
        self.students.sort()
        self.first_row_group = separete_plants_in_subgroups(list(self.first_row))
        self.second_row_group = separete_plants_in_subgroups(list(self.second_row))

    def plants(self, student: str) -> list:
        """ return the plants that the student is responsable for """
        plants_of_students = []
        index_student = self.students.index(student)
        for item in self.first_row_group[index_student]:
            plants_of_students.append(item)
        for item in self.second_row_group[index_student]:
            plants_of_students.append(item)
        return convert_initial_4_name(plants_of_students)
