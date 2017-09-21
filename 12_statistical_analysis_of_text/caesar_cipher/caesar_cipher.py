# -*- coding: utf-8 -*-
"""
    Created on 31.08.2017 14:18
    @author: Kristoffer-Andre Kalliainen
"""
import string


def caesar_encode(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


print(caesar_encode("This is a test string!", 20))
print(caesar_encode("Tbcm cm u nymn mnlcha!", -20))
