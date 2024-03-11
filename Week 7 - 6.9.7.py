import math


def to_secs (hours, minutes, seconds):
    a = (hours * 3600)
    b = (minutes * 60)
    c = seconds
    result = a + b + c
    return result
