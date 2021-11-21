#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 6

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def f(ll):
  ll = list(ll)
  ix = max(range(len(ll)),key=lambda x: ll[x])
  v = ll[ix]
  ll[ix] = 0

  for jx in range(ix+1, ix+1+v):
    ll[jx % len(ll)] += 1
  
  return tuple(ll)

def part1(rows, iobj):
  ll = tuple(iobj.ints())
  
  return detect_cycle(ll, f)['end']

def part2(rows, iobj):
  ll = tuple(iobj.ints())

  return detect_cycle(ll, f)['len']


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
