def rotate(text, key):
    result = ""

    for caracter in text:
        if caracter.isalpha():
            base = ord("A") if caracter.isupper() else ord("a")
            new_char = chr((ord(caracter) - base + key) % 26 + base)
            result += new_char
        else:
            result += caracter
    return result
