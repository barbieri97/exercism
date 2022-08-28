""" code to phone number exercise """
from string import punctuation, ascii_letters

class PhoneNumber:
    """ clean a phone number """
    def __init__(self, number):
        check_number = ''.join(item for item in number if item not in '+()- .')


        for item in check_number:
            # if a phone number has punctuation in place of some digits.
            if item in punctuation:
                raise ValueError("punctuations not permitted")
            # if a phone number has letters in place of some digits.
            if item in ascii_letters:
                raise ValueError("letters not permitted")
        # if a phone number has less than 10 digits.
        if len(check_number) < 10:
            raise ValueError("incorrect number of digits")
        # if a phone number has more than 11 digits.
        if len(check_number) > 11:
            raise ValueError("more than 11 digits")
        # if a phone number has 11 digits, but starts with a number other than 1.
        if len(check_number) == 11 and check_number[0] != '1':
            raise ValueError("11 digits must start with 1")
        # if a phone number has an exchange code that starts with 0.
        if check_number[-7] == '0':
            raise ValueError("exchange code cannot start with zero")
        # if a phone number has an exchange code that starts with 1.
        if check_number[-7] == '1':
            raise ValueError("exchange code cannot start with one")
        # if a phone number has an area code that starts with 0.
        if check_number[-10] == '0':
            raise ValueError("area code cannot start with zero")
        # if a phone number has an area code that starts with 1.
        if check_number[-10] == '1':
            raise ValueError("area code cannot start with one")

        self.number = check_number[-10:]
        self.area_code = self.number[:3]

    def __repr__(self):
        return f'{self.number}'

    def pretty(self):
        """ create a pretty string to print the number """
        area_code = f'({self.area_code})'
        exchenge_number = self.number[3:6]
        subscriber_number = self.number[6:]
        return '-'.join(item for item in [area_code, exchenge_number, subscriber_number])
