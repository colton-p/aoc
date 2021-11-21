#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ll = iobj.numeric_tuples()

  return sum(max(row) - min(row)for row in ll)

def part2(rows, iobj):
  ll = iobj.numeric_tuples()
  s = 0
  for row in ll:
    for t in itertools.combinations(row, 2):
        if max(t) % min(t) == 0:
          s += max(t) // min(t)


  return s


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
