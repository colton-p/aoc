#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

# TODO: how smart to make this?
rows = input_rows(1, year=2015)

(kind, rows, min_row, max_row, _x) = analyze_input(rows)
print("  Kind: %s" % kind)
print("n rows: %4d" % rows)
if min_row == max_row:
  print("n cols: %4d" % (max_row))
else:
  print("n cols: %4d-%4d" % (min_row, max_row))
print('.' * 16)
print('')

string = input_as_single_string(1, year=2015)

def part1(s):
  return sum([1 for x in s if '(' == x]) + sum([-1 for x in s if ')' == x])


def part2(s):
  v = 0

  # TODO: first position with predicate?
  for (ix,c) in enumerate(s):
    if c == '(':
      v += 1
    else:
      v -= 1

    if v < 0:
      return ix + 1

print('P1', part1(string))
print('P2', part2(string))
