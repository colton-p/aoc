#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 20

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def evolve(state):
  (pos, v, a) = state
  for ix in range(len(pos)):
    if pos[ix] is None:
      continue
    v[ix] = vadd(v[ix], a[ix])
    pos[ix] = vadd(pos[ix], v[ix])
  
  return pos, v, a
  
def closest(state):
  (pos, v, a) = state 
  return min(range(len(pos)),key=lambda x: pos[x] is not None and vdist1(pos[x], [0,0,0]) or 999999999999)

def destroy_dups(pos):
  c = Counter([tuple(x) for x in pos if x])

  for ix in range(len(pos)):
    if pos[ix] is None: continue
    if c[tuple(pos[ix])] > 1:
      pos[ix] = None

def part1(rows, iobj):
  ll = iobj.numeric_tuples()

  pos = [head(x, 3) for x in ll]
  v = [x[3:6] for x in ll]
  a = [tail(x, 3) for x in ll]

  return detect_constant( (pos, v, a), transition_func=evolve, scoring_func=closest)

def part2(rows, iobj):
  ll = iobj.numeric_tuples()

  pos = [head(x, 3) for x in ll]
  v = [x[3:6] for x in ll]
  a = [tail(x, 3) for x in ll]

  def update(state):
    (pos, v, a) = state
    evolve(state)
    destroy_dups(pos)
    return (pos, v, a)

  return detect_constant(
    (pos, v, a),
    transition_func=update,
    scoring_func=lambda x: len(compact(x[0]))
  )


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
