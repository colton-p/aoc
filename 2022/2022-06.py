from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 6

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  for (ix, a) in enumerate(each_cons(ss, 4)):
    if len(set(a)) == 4:
      return ix + 4

  return

def part2(rows, iobj):
  for (ix, a) in enumerate(each_cons(ss, 14)):
    if len(set(a)) == 14:
      return ix + 14

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
