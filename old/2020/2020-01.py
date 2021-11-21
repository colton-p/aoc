from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  for x in its.permutations(ll, 2):
    if sum(x) == 2020:
      return prod(x)

  return

def part2(rows, iobj):
  for x in its.permutations(ll, 3):
    if sum(x) == 2020:
      return prod(x)

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
