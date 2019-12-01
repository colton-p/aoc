#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2015
DAY = 1

iobj = Input.for_date(DAY, year=YEAR)
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):
  s = iobj.single_string()

  return sum([1 for x in s if '(' == x]) + sum([-1 for x in s if ')' == x])

def part2(rows, iobj):
  s = iobj.single_string()

  v = 0

  for (ix,c) in enumerate(s):
    if c == '(':
      v += 1
    else:
      v -= 1

    if v < 0:
      return ix + 1


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
