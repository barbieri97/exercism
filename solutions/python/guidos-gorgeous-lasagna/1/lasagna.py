# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(temp: int) -> int: 
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - temp

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

def preparation_time_in_minutes(layers: int) -> int:
    """ Essa função fornece o tempo de praparo da lasanha 
    dado o numero de camadas que deseja fazer """
    return layers * PREPARATION_TIME 

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """ Essa função, dado o numero de camadas feita e o tempo ja
    passado de cozimento, devolve o tempo total já gasto no preparo 
    da lasanha """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time
