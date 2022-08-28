"Learn about strings by helping your little sister with her vocabulary homework."

def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return f'un{word}'


def make_word_groups(vocab_words: list):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """

    prefix = vocab_words[0]
    for i, j in enumerate(vocab_words):
        if j != prefix:
            vocab_words[i] = f'{prefix + j}'
    return ' :: '.join(x for x in vocab_words)



def remove_suffix_ness(word: str):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    vogals = 'aeiou'
    w_ness = word.replace('ness', '')

    if w_ness[-1] == 'i' and w_ness[-2] not in vogals:
        w_ness = w_ness.replace(f'{w_ness[-2] + w_ness[-1]}', f"{w_ness[-2] + 'y'}")


    return w_ness


def adjective_to_verb(sentence: str, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    adjective_2_verb = sentence.split()[index].rstrip('.!?')

    return adjective_2_verb + 'en'
