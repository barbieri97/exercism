""" code to Matching Brackets exercise """
import re


def is_paired(input_string: str) -> bool:
    """
    :param input_string: str - strinf to verify brackets
    :return: bool - True if all brackets are matched
    """
    brackets = {
    ')' : '(',
    ']': '[',
    '}':'{'
    }
    chaves = []
    for item in input_string:
        if item in brackets.values():
            chaves.append(item)
        elif item in brackets:
            if not chaves:
                return False
            if chaves.pop() != brackets[item]:
                return False
    return not chaves
    