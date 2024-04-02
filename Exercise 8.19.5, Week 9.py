import sys

import string

best_quote = """Would you believe in what you believed in if you were the only one that believed it? Ask yourself, and figure out why."""


punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

wds = remove_punctuation(best_quote).split()

def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

def EWord_Count(words):
    e_words = 0
    for x in words:
        if find(x, 'e') != -1:
            e_words += 1
    return e_words



best_quote = """Would you believe in what you believed in if you were the only one that believed it? Ask yourself, and figure out why."""
removed_quote = remove_punctuation(best_quote)
fav_string = removed_quote.split()
total_words = len(fav_string)
e_words = EWord_Count(fav_string)

def print_statement(total_words, e_words):
    e_percentage = (e_words/total_words) * 100
    print("Your text contains " + str(total_words) + " words, of which " + str(e_words) + " ( " + str(e_percentage) + " %) contain an 'e'.")

def main():
    print_statement(total_words, e_words)

main()

