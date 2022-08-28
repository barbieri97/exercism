""" solution to pangram exercise """

from collections import Counter


def is_pangram(sentence: str) -> bool:
    """ return True if the sentence is a pangran """
    clean_sentence = sentence.lower()
    for item in clean_sentence:
        if not item.isalpha():
            clean_sentence = clean_sentence.replace(item, '')
    words = Counter(clean_sentence)
    return len(words) == 26
