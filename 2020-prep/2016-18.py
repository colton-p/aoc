#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2016
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

RULES = {
  '...': '.',
  '..^': '^',
  '.^.': '.',
  '.^^': '^',
  '^..': '^',
  '^.^': '.',
  '^^.': '^',
  '^^^': '.',
}

def part1(rows, iobj):
  ca = CA1(iobj.single_string(), RULES)

  c = 0
  for (ix, ss) in enumerate(ca.evolve_n(40-1)):
    c += sum([1 for x in ss.values() if x == '.'])

  return c

def part2(rows, iobj):
  ca = CA1(iobj.single_string(), RULES)

  c = 0
  for ss in ca.evolve_n(400000-1):
    c += sum([1 for x in ss.values() if x == '.'])

  return c



print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
