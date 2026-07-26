def rotate(text, key):
    result = ""

    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            new_char = chr((ord(c) - base + key) % 26 + base)
            result += new_char
        else:
            result += c
    return result
