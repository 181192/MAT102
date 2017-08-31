# -*- coding: utf-8 -*-
"""
    Created 31.08.2017 14:52

    @author Kristoffer-Andre Kalliainen
"""
import os
from collections import Counter
from string import ascii_lowercase

filename = "../TekstFiler/macbeth"


def file_check(fn):
    try:
        open(fn, "r")
        return 1
    except IOError:
        print("Error: Filen ser ikke ut til å eksistere")
        return 0


def write_seed_file(fn):
    if not file_check(fn):
        return 0
    file = open(fn, "w")
    file.write("Hello World\n")
    file.write("This is our new text file\n")
    file.write("and this is another line.\n")
    file.write("Why? Because we can!\n")
    file.close()


def count_characters(fn):
    infile = open(fn, 'r')
    characters = 0
    for line in infile:
        line = line.strip(os.linesep)
        characters = characters + len(line)
    return characters


def count_letters(fn):
    with open(fn) as f:
        counter = Counter(letter for line in f
                          for letter in line.lower()
                          if letter in ascii_lowercase)

        print("| Antall bokstaver:\t\t| Antall prosent:")
        for key, value in counter.most_common():
            print("|", key, "=", value, "\t\t\t\t|", key, "=",
                  float("{0:.3f}".format((value / count_characters(fn)) * 100)))


# write_seed_file(filename)
if not file_check(filename):
    exit(0)
count_letters(filename)
