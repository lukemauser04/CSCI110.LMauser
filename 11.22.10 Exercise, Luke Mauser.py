import os

import string

import sys

def replace(s, old, new):
        splt = s.split(old)

        return new.join(splt)


def test (did_pass):
    """   Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format (linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print (msg)

def main():
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

    new_string = replace(s, "om", "am")

    print(new_string)
    
main()
