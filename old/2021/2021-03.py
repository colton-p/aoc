from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 3

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):
  def count(ix):
    if sum(int(row[ix]) for row in rows) > len(rows) / 2:
      return '1', '0'
    return '0', '1'

  cs = [count(ix) for ix in range(len(rows[0]))]

  gamma = int(''.join(x[0] for x in cs), 2)
  epsilon = int(''.join(x[1] for x in cs),2)

  return gamma * epsilon

def part2(rows, iobj):

  def count(L, ix):
    if sum(int(r[ix]) for r in L) >= len(L) / 2:
      return '1', '0'
    return '0', '1'
  
  highs, lows = list(rows), list(rows)

  for ix in range(len(highs[0])):
    hi, _ = count(highs, ix)
    _, lo = count(lows, ix)

    highs = [l for l in highs if l[ix] == hi]
    if len(lows) > 1:
      lows = [l for l in lows if l[ix] == lo]
    
  
  (hi,) = highs
  (lo,) = lows

  return int(hi, 2) * int(lo, 2)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
