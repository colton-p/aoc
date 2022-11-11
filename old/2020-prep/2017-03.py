#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 3

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  tgt = iobj.ints()[0]
  for (_ix, pt) in zip(range(tgt), util.GridIterators.spiral()):
    pass

  return sum(map(abs, pt))


def part2(rows, iobj):
  tgt = iobj.ints()[0]
  g = defaultdict(int)

  for pt in util.GridIterators.spiral():
    g[pt] = sum([g[p] for p in rect_adj(pt, diag=True)]) or 1
    
    if g[pt] > tgt:
      return g[pt]


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
