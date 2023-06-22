'''Finding the percentage of G's and C's in a DNA string'''

import collections

import sys

DNA = collections.Counter(sys.stdin.read())
NUM = DNA['G'] + DNA['C']
DEN = NUM + DNA['A'] + DNA['T']
if DEN == 0:
    print("0.000")
else:
    print(round(NUM / DEN * 100, 3))
