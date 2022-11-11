from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 7

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def f(n):
  return n * (n+1) // 2

def part1(rows, iobj):
  L = list(ints(ss))

  a = []
  for i in range(0, max(L)):
    a += [(sum((abs(v-i)) for v in L), i)]

  return min(a)
  ### return min( sum(abs(v-i) for v in L) for i in range(0, max(L)))

def part2(rows, iobj):
  L = list(ints(ss))
  return min( sum(f(abs(v-i)) for v in L) for i in range(0, max(L)))

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
