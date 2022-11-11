#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):

  def f(x):
    c = Counter(x)
    return 2 in c.values()
  def g(x):
    c = Counter(x)
    return 3 in c.values()
  

  return quantify(rows, f) * quantify(rows, g)


def part2(rows, iobj):

  def f(a, b):
    return quantify(zip(a,b), lambda x: x[0] != x[1])


  (x,y) = detect(combinations(rows, 2), lambda x: f(*x) == 1)

  return ''.join(set(x) & set(y))




print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
