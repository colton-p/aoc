#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 4

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ss = iobj.tuples()

  def f(row):
    return len(row) == len(set(row))

  return quantify(ss, f)



def part2(rows, iobj):
  def f(row):
    for (x,y) in itertools.combinations(row, 2):
      if set(x) == set(y):
        return False
    return True

  return quantify(iobj.tuples(), f)


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
