#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 5

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ll = iobj.int_list()

  ix = 0
  c = 0
  while True:
    jmp = ll[ix]
    ll[ix] += 1
    ix += jmp
    c += 1
    if ix >= len(ll):
        break

  return c


def part2(rows, iobj):
  ll = iobj.int_list()

  ix = 0
  c = 0
  while True:
    jmp = ll[ix]
    if jmp >= 3:
      ll[ix] -= 1
    else:
      ll[ix] += 1
    ix += jmp
    c += 1
    if ix >= len(ll):
        break

  return c

print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
