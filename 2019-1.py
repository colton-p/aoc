#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.pp_analyze()
iobj.peak()
rows = list(iobj.rows)

def part1(rows, iobj):


  ll = iobj.int_list()
  return sum([x // 3 - 2 for x in ll])


def f(x):
  s = 0

  while x > 0:
    x = x // 3 -2

    if x < 0:
      break
    s+=x


  return s

def part2(rows, iobj):
  ll = iobj.int_list()

  return sum([f(x) for x in ll])


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
