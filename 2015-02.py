#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2015
DAY = 2

# TODO: how smart to make this?
rows = input_rows(DAY, year=YEAR)

(kind, rows, max_row, min_row, _x) = analyze_input(rows)
print("  Kind: %s" % kind)
print("n rows: %4d" % rows)
if min_row == max_row:
  print("n cols: %4d" % (max_row))
else:
  print("n cols: %d-%d" % (min_row, max_row))
print('.' * 16)
print('')



rows = input_as_numeric_tuples(DAY, year=YEAR)
print(rows)


def part1(s):

  return sum([min([l*w, w*h, h*l]) + 2*l*w + 2*w*h + 2*h*l for (l,w,h) in s])


def part2(s):

  return sum([
    sum(min( [(l,w), (w,h), (l,h)], key=lambda x: x[0]*x[1])) * 2 + l*w*h
  for (l,w,h) in s])

print('P1', part1(rows))
print('P2', part2(rows))
