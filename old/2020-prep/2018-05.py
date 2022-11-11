#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 5

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def chk(x, y):
  return x != y and x.lower() == y.lower()

def f(s):
  out = collections.deque('.')

  while len(s):
    x = out.pop()
    y = s.popleft()

    if chk(x, y):
      continue
    else:
      out.append(x)
      out.append(y)

  out.popleft()
  return out

def part1(rows, iobj):
  return len(f(collections.deque(iobj.single_string())))


def g(s, x):
  s = collections.deque(c for c in s if c.lower() != x)
  return len(f(s))


def part2(rows, iobj):
  s = iobj.single_string()
  return min(g(s,x) for x in set(s))


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
