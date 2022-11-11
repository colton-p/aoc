#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 11

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  d = {
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'sw': (-1, 0, 1),
    'ne': (1, 0, -1),
    'nw': (-1, 1, 0),
    'se': (1, -1, 0),

  }
  pt = (0,0,0)
  for step in rows[0].split(','):
    pt = vadd(pt, d[step])

  return max(map(abs,pt))


def part2(rows, iobj):
  d = {
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'sw': (-1, 0, 1),
    'ne': (1, 0, -1),
    'nw': (-1, 1, 0),
    'se': (1, -1, 0),

  }
  pt = (0,0,0)
  m = 0
  for step in rows[0].split(','):
    pt = vadd(pt, d[step])

    m = max(m, max(map(abs,pt)))

  return m


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
