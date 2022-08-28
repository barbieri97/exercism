""" Calculate the Hamming Distance between two DNA strands. """

def distance(strand_a: str, strand_b: str) -> int:
    """
    :param strand_a: str - sequence of DNA
    :pararm strand_b: str - sequence of DNA
    :return: int - number of diferences between the sequences of DNA
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    err = 0
    for item_a, item_b in zip((strand_a), (strand_b)):
        if item_a != item_b:
            err += 1
    return err
