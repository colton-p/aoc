#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 14

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def ev(state):
  (L, ix, jx) = state

  new = str(L[ix] + L[jx])

  L += map(int, new)
  ix += L[ix] + 1
  ix %= len(L)

  jx += L[jx] + 1
  jx %= len(L)


  return (L, ix, jx)

def part1(rows, iobj):

  L = [3, 7]
  ix = 0
  jx = 1
  state = (L, ix, jx)


  tgt = iobj.single_int()
  (M, _, _) = evolve_n(state, ev, tgt+10)
  return ''.join(map(str, M[tgt:tgt+10]))

def part2(rows, iobj):
  L = [3, 7]
  ix = 0
  jx = 1
  state = (L, ix, jx)

  tgt = iobj.single_string()
  tgt = list(map(int, list('170641')))
  ix = 0

  while ix <= 16_000_000:
    ix +=1

    state = ev(state)
    L = state[0]


    if L[-len(tgt):] == tgt:
      return len(L) - len(tgt)
    if L[-len(tgt)-1:-1] == tgt:
      return len(L) - len(tgt) - 1


  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
