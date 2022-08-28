""" code to alergies exercise """

class Allergies:
    """ doc string """

    _allergies = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        """ doc string """
        return bool(self.score & self._allergies[item])


    @property
    def lst(self):
        """ doc string """
        return [item for item in self._allergies if self.allergic_to(item)]
