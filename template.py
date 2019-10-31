#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = <year>
DAY = <day>

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





def part1(s):

  return


def part2(s):

  return


print('P1', part1(rows))
print('P2', part2(rows))
