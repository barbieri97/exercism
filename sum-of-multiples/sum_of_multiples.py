""" doc string """
def sum_of_multiples(limit, multiples):
    """ doc string """
    list_multiples = []
    for item in multiples:
        if item != 0:
            for number in range(1, limit):
                if number % item == 0 and number not in list_multiples:
                    list_multiples.append(number)
    return sum(list_multiples)
