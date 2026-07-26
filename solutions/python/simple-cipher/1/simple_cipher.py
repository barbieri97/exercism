""" doc string """
from random import choices
from string import ascii_lowercase
from itertools import cycle
class Cipher:
    """ doc string """
    def __init__(self, key=choices(ascii_lowercase, k=100)):
        self.key = ''.join(item for item in key)

    def encode(self, text):
        """ doc string """
        return ''.join(
            chr(((ord(char) - 2 * ord('a') + ord(key)) % 26) + ord('a'))
            for char, key in zip(text, cycle(self.key))
        )
    def decode(self, text):
        """ doc string """
        return ''.join(
            chr(((ord(char) - ord(key) + 26) % 26) + ord('a'))
            for char, key in zip(text, cycle(self.key))
        )
