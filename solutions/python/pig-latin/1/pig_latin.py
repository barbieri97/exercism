VOWELS = "aeiou"


def translate(text: str) -> str:
    return " ".join(_translate_word(word) for word in text.split())


def _translate_word(word: str) -> str:
    if word[0] in VOWELS or word.startswith(("xr", "yt")):
        return word + "ay"
        
    i = 0
    while i < len(word) and word[i] not in VOWELS and not (word[i] == "y" and i > 0):
        i += 1

    if i < len(word) and word[i] == "u" and word[i - 1] == "q":
        i += 1

    return word[i:] + word[:i] + "ay"