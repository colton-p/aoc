#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 22

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):

  G = Grid.from_rows(rows)

  pos = (12, 12)
  dir = DIR.UP

  c = 0
  for _i in range(10_000):
    if G[pos] == '#':
      dir = turn_right(dir)
      G[pos] = '.'
    else:
      dir = turn_left(dir)
      G[pos] = '#'
      c += 1
    pos = tuple(vadd(pos, dir))

  return c


S = namedtuple('S', 'pos dir G c')
def part2(rows, iobj):
  G = Grid.from_rows(rows)

  pos = (12, 12)
  dir = DIR.UP
  c = 0

  for _i in range(10_000_000):
    v = G[pos]
    if v == '.':
      dir = turn_left(dir)
      G[pos] = 'W'
    elif v == 'W':
      dir = dir
      c += 1
      G[pos] = '#'
    elif v == '#':
      dir = turn_right(dir)
      G[pos] = 'F'
    elif v == 'F':
      dir = turn_right(turn_right(dir))
      G[pos] = '.'
    else:
      assert False, (pos, v)
      
    pos = tuple(vadd(pos, dir))

  return c

print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
