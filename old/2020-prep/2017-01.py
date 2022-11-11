from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2017
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):

  ss = iobj.single_string()
  ss += ss[0]

  return quantify(each_cons(ss), lambda x: x[0] == x[1] and int(x[0]) or 0)

def part2(rows, iobj):
  ss = list(map(int, iobj.single_string()))

  def f(ix, v):
    if v == ss[(ix + len(ss) // 2) % len(ss)]:
      return v

  return quantify(enumerate(ss), lambda x: f(*x))

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
