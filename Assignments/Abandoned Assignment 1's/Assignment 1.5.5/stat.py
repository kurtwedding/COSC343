import os, io, sys
import locale
from functools import cmp_to_key
import importlib
import traceback
import time
from settings import game_settings
language = "english"
file = os.path.join("dictionaries", "%s.txt" % language)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphNumber = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numLetters = 0
probDict = []
f = open("results.csv", "w")


# Code taken directly from the wordle.py script
def read_dictionary(file_path, word_length=None):
    with io.open(file_path, mode="r", encoding="iso-8859-15") as f:
        words = f.read()
        words = words.split("\n")
        try:
            i = words.index("<support>")
            words = [words[:i], words[i + 1:]]
        except:
            words = [words]

        dictionary = []
        for i in range(len(words)):
            words[i] = map(lambda x: x.upper(), words[i])
            if word_length is not None:
                words[i] = filter(lambda x: len(x) == word_length, words[i])
            words[i] = list(
                filter(lambda x: "'" not in x and " " not in x and "/" not in x and "-" not in x and "." not in x,
                       words[i]))
            words[i] = list(words[i])
            dictionary += words[i]

    locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")

    letters = list({l for word in dictionary for l in word})
    letters = sorted(letters, key=cmp_to_key(locale.strcoll))

    solutions = words[0]

    return solutions, dictionary, letters


def sortSecond(val):
    return val[1]

if __name__ == "__main__":
    sol, dictio, lett = read_dictionary(file, 5)
    f.write("Letter,Occurances,Probability\n")
    for wrd in dictio:
        for letter in wrd:
            letter = letter.lower()
            alphNumber[alphabet.index(letter)] += 1
            numLetters += 1

    for element in range(len(alphabet)):
        f.write(str(alphabet[element]) + "," + str(alphNumber[element]) + "," + str(round(alphNumber[element]/numLetters*100, 2)) + "%\n")

    f.close()
