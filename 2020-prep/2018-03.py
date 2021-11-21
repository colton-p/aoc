#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 3

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):

  d = defaultdict(int)

  for (ix, x, y, dx, dy) in iobj.numeric_tuples():
    for (px, py) in itertools.product(range(x, x+dx), range(y, y+dy)):
      d[(px,py)] += 1

  return quantify(d.values(), lambda x: x >= 2)


def part2(rows, iobj):
  d = defaultdict(int)

  for (ix, x, y, dx, dy) in iobj.numeric_tuples():
    for (px, py) in itertools.product(range(x, x+dx), range(y, y+dy)):
      d[(px,py)] += 1

  for (ix, x, y, dx, dy) in iobj.numeric_tuples():
    it = itertools.product(range(x, x+dx), range(y, y+dy))
    if all(d[(px,py)] == 1 for (px, py) in it):
      return ix

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
