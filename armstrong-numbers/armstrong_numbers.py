""" my code to armstrong-number exercise """

def is_armstrong_number(number):
    """ return True if is Armstrong number, else return False """
    expoente = len(str(number))
    total = 0
    for item in str(number):
        total += int(item) ** expoente
    return total == number
