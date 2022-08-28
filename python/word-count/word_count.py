""" function to help count how many each word have in a phrase """

def count_words(sentence: str) -> dict:
    """
    :param sentence: str - sentence to count each one of his words
    :return: dict - dictionary with the numbers of each word
    """
    formated_sentece = remove_special_characters_and_formatation(sentence).lower()
    list_of_words_without_quotations = [item.strip("'") for item in formated_sentece.split()]
    words_without_repetition = set(list_of_words_without_quotations)

    return{key: list_of_words_without_quotations.count(key) for key in words_without_repetition}


def remove_special_characters_and_formatation(sentence: str) -> str:
    """
    return a string without special characters and formatation
    """
    for item in ('\n', '\t', ',', '_', '.', ':', '!', '&', '@', '$', '%', '^', '&', ):
        if item != ".":
            sentence = sentence.replace(item, ' ')
        else:
            sentence = sentence.replace(item, '')
    return sentence