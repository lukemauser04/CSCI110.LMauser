import sys

import math


def to_secs (hours, minutes, seconds):
    a = (hours * 3600)
    b = (minutes * 60)
    c = seconds
    result = a + b + c
    return result

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # This gets the callers line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(to_secs(2, 30, 11) == 9011)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)
