""" code to collatz conjecture exercise """
def steps(number: int) -> int:
    """
    Return the number of steps until reach 1
    :param number: int - number to initailize the steps
    :return: int - number of steps until reach 1
    """
    if number < 1:
        raise ValueError('Only positive integers are allowed')
    step = 0
    operation = lambda n: n/2 if n % 2 == 0 else (n*3) + 1
    while number != 1:
        number = operation(number)
        step += 1
    return step
