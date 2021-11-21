#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 25

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

R = {}

for lines in each_slice(rows[3:], 10):
  src = lines[0][-2]
  (v0,) = ints(lines[2])
  d0 = 1 if lines[3].split(' ')[-1] == 'right.' else -1
  tgt0 = lines[4][-2]

  (v1,) = ints(lines[6])
  d1 = 1 if lines[7].split(' ')[-1] == 'right.' else -1
  tgt1 = lines[8][-2]

  R[(src, 0)] = (v0, d0, tgt0)
  R[(src, 1)] = (v1, d1, tgt1)


def part1(rows, iobj):
  (chk_steps,) = ints(rows[1])

  cell = 'A'
  T = defaultdict(int)
  ix = 0

  s0 = (cell, T, ix)

  def update(state):
    (cell, T, ix) = state
    (v, d, tgt) = R[(cell, T[ix])]

    T[ix] = v
    return (tgt, T, ix+d)

  sx = evolve_n(s0, update, chk_steps)

  return sum(sx[1].values())


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
