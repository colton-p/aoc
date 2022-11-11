from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2015
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)
ss = iobj.single_string()
ll = iobj.int_list()

def part1(rows, iobj):
  return ss.count('(') - ss.count(')')

def part2(rows, iobj):
  s = 0
  for (ix,x) in enumerate(ss):
    s += (x == '(' and 1 or -1)
    if s < 0:
      return ix + 1

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
