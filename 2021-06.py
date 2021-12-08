from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 6

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def evolve(C):
  d = Counter({ (k-1): v for (k, v) in C.items()})
  if -1 in d:
    d[8] = d[-1]
    d[6] += d[-1]
    del d[-1]

  return d

def part1(rows, iobj):
  d = Counter(ints(ss))
  for i in range(80):
    d = evolve(d)

  return sum(d.values())

def part2(rows, iobj):
  d = Counter(ints(ss))
  for i in range(256):
    d = evolve(d)

  return sum(d.values())

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
