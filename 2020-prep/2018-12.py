#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 12

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


rules = {}

def evolve(state):
  new = defaultdict(lambda: '.')
  for ix in range( min(state.keys())-5, 5+max(state.keys()) ):
    sub = tuple([state[j] for j in range(ix-2, ix+3)])
    new[ix] = rules[sub]
  
  return new



def part1(rows, iobj):
  global rules
  s0 = rows[0].split(':')[1].strip()

  s = defaultdict(lambda: '.', enumerate(s0))

  rules = {tuple(x[0]): x[2] for x in iobj.tuples()[2:]}

  s = evolve_n(s, evolve, 20)
  return sum(i for i in s if s[i] == '#')


def part2(rows, iobj):
  s0 = rows[0].split(':')[1].strip()
  s = defaultdict(lambda: '.', enumerate(s0))

  v = 0
  for ix in range(200):
    s = evolve(s)
    v0 = v
    v = sum(i for i in s if s[i] == '#')
  
  d = v - v0

  return (50_000_000_000 - 200) * d + v


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
