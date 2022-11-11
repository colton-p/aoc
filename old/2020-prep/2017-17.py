#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 17

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def f(L, ix, ins):
  return L[:ix] + [ins] + L[ix:]


def part1(rows, iobj):
  (step,) = iobj.int_list()

  L = [0]
  ix = 0
  for ins in range(1, 2018):
    ix = (ix + step) % len(L) + 1
    L = f(L, ix, ins)

  return L[ix+1]


def part2(rows, iobj):
  (step,) = iobj.int_list()
  ix = 0

  target = None
  for ins in range(1, 50_000_000):
    ix = (ix + step) % ins + 1
    if ix == 1:
      target = ins

  return target


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
