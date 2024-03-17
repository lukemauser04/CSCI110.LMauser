import sys

import math

def print_triangular_numbers(n):
    for x in range (1, n + 1):
        print(x, x * (x + 1) / 2)
