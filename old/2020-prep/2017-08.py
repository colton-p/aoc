#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 8

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  R = defaultdict(int)

  for (tgt, op, val, _if, cmp_tgt, cmp_op, cmp_val) in iobj.tuples():
    if eval(f"{R[cmp_tgt]} {cmp_op} {cmp_val}"):
      if op == 'inc':
        R[tgt] += val
      elif op == 'dec':
        R[tgt] -= val
      else:
        assert False, op

  return max(R.values())


def part2(rows, iobj):
  R = defaultdict(int)
  m = 0

  for (tgt, op, val, _if, cmp_tgt, cmp_op, cmp_val) in iobj.tuples():
    if eval(f"{R[cmp_tgt]} {cmp_op} {cmp_val}"):
      if op == 'inc':
        R[tgt] += val
      elif op == 'dec':
        R[tgt] -= val
      else:
        assert False, op

    m = max(m, max(R.values()))


  return m


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
