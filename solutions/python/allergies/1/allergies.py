""" code to alergies exercise """
def _binary(number):
    """ return a string that correspond to binary number """
    list_binary = []
    while number >= 1:
        number, binary = divmod(number, 2)
        list_binary.append(binary)
    # retorna o numero binario ao contrario para que a casa da unidade corresponda com o index 0
    return ''.join(str(item) for item in list_binary[:8])

class Allergies:
    """ doc string """

    _allergies = [
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats'
        ]

    def __init__(self, score):
        # preeche com 0 os numeros binarios com menos de 8 bits
        self.binary = _binary(score).ljust(8, '0')

    def allergic_to(self, item):
        """ doc string """
        index = self._allergies.index(item)
        return self.binary[index] == '1'
        


    @property
    def lst(self):
        """ doc string """
        return [item for item in self._allergies if self.allergic_to(item)]