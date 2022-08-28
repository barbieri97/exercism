""" code to anagram exercise """

def find_anagrams(word: str, candidates: list) -> list:
    """
    Find the possible anagrams of the word
    :param word: str - string to find his anagrams
    :param candidates: list[str] - list of the candidates to anagram
    :return: list[str] - list of the anagrams
    """
    w_low = word.lower()
    return [i for i in candidates if sorted(w_low) == sorted(i.lower()) and w_low != i.lower()]
