""" module to verify a credid card number"""

class Luhn:
    """ verify a credid card nuber with Luhn algorithm """
    def __init__(self, card_num: str):
        # remove os espaços em brancos
        self.num_str = card_num.replace(' ', '')

    def valid(self):
        """ given a number, return True if is a valid credid card number """
        if not self.num_str.isdigit() or self.num_str == '0':
            return False
        #converte em lista e invewrte para ficar mais facil de acessar os numeros
        list_num = [int(item) for item in self.num_str][::-1]
        # lista com os primeros numeros (index par)
        list_first_numbers = list_num[0::2]
        # lista com os segundos numeros (index inpar)
        list_second_numbers = list_num[1::2]
        # duplicando os segundos numeros
        num_duplicated = [sum(divmod(item*2, 10)) for item in list_second_numbers]
        return (sum(list_first_numbers) + sum(num_duplicated)) % 10 == 0
    