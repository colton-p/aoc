from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 4

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  cc = 0
  iobj.numeric_tuples()
  for (a, b, x, y) in nts:
    b = abs(b)
    y = abs(y)
    print(a,b, x, y)

    l = set(range(a, b+1))
    r = set(range(x, y+1))
    print(l, r, l <= r, r <= l)

    if l & r:
      cc += 1

  return cc

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
