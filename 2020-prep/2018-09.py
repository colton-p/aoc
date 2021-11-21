#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 9

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

N_PLAYERS, LAST_MARBLE = ints(rows[0])

def update(state):
  (L, to_ins, player, scores) = state

  if to_ins % 23 == 0:
    L.rotate(7)
    scores[player] += L.popleft() + to_ins
  else:
    L.rotate(-2)
    L.appendleft(to_ins)

  return (L, to_ins + 1, (player + 1) % N_PLAYERS, scores)


def part1(rows, iobj):
  state = ( collections.deque([0]), 1, 1, defaultdict(int))
  state = evolve_n(state, update, LAST_MARBLE)
  return max(state[-1].values())


def part2(rows, iobj):
  state = ( collections.deque([0]), 1, 1, defaultdict(int))
  state = evolve_n(state, update, LAST_MARBLE * 100)
  return max(state[-1].values())


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
