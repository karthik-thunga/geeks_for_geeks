# Given an integral number N. The task is to find the count of digits present in this number.
import math

def count_digits(N):
    return math.floor(math.log10(N)) + 1