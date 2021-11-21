from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 5

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()
ww = iobj.word_tuples()

def chk(s):
  rr = list(range(128))
  ss = list(range(8))
  for c in head(s, 7):
    if c == 'F':
      rr = head(rr, len(rr) // 2)
    else:
      rr = tail(rr, len(rr) // 2)

  for c in tail(s, 3):
    if c == 'L':
      ss = head(ss, len(ss) // 2)
    else:
      ss = tail(ss, len(ss) // 2)
  
  return rr[0] * 8 + ss[0]

def part1(rows, iobj):


  return max(chk(row) for row in rows)

def part2(rows, iobj):

  vals = [chk(row) for row in rows]
  (lo, hi) = min(vals), max(vals)
  return set(range(lo, hi)) - set(chk(row) for row in rows)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
