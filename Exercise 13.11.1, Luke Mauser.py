
import os

import sys

myfile = open("test.txt", "w")
myfile.write("Hello World!\n")
myfile.write("What a day is has been,\n")
myfile.write("I will be going now.\n")

f = open("test.txt", "r")
xs = f.readlines()
f.close()

xs.sort()


g = open("test.txt", "w")
xs.reverse()
for line in xs:
    f.write(line)
g.close()


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


test(myfile)

print (myfile)
