from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 9

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  def chk(l):
    assert len(l) == 26
    for x in its.combinations(l[:-1], 2):
      if sum(x) == l[-1]:
        return True
    return False
  
  for x in each_cons(iobj.int_list(), n=26):
    if not chk(x):
      return x[-1]

  return

def part2(rows, iobj):
  TGT = 1721308972

  for sz in range(2, 1000):
    for x in each_cons(iobj.int_list(), n=sz):
      if sum(x) == TGT:
        return min(x) + max(x)

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
