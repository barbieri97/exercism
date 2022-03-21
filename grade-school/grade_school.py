""" Class to help add children to his grade """

class School:
    """ manage the children grades """

    def __init__(self):
        self.students = [] # to verify if the studests already beadd to any grade
        self.grades: dict = {}
        self.add_successful = []

    def add_student(self, name, grade):
        """ add student to a grade if the student not in any grade """
        if grade not in self.grades:
            self.grades[grade] = []
        if name in self.students:
            self.add_successful.append(False)
            return None
        self.grades[grade].append(name)
        self.students.append(name)
        self.add_successful.append(True)
        return None

    def roster(self):
        """ return a list of all students ordered by the grade and the name """
        sorted_students = []
        keys = list(self.grades.keys())
        keys.sort()
        for index in keys:
            values = self.grades.get(index)
            values.sort()
            for item in values:
                sorted_students.append(item)
        return sorted_students

    def grade(self, grade_number):
        """ Return a list of the students in 'grade_number' ordered by name """
        if grade_number not in self.grades:
            return []
        grade_students = self.grades.get(grade_number)
        grade_students.sort()
        return grade_students

    def added(self):
        """ Return the historic of the add students add """
        return self.add_successful
