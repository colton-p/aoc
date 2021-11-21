from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2015
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):

  def f(x):
    (l,w,h) = x
    sides = [prod(v) for v in itertools.combinations(x, 2)]

    return sum(sides) * 2 + min(sides)

  return quantify(iobj.numeric_tuples(), f)

def part2(rows, iobj):

  def f(x):
    return prod(x) + 2*(sorted(x)[0] + sorted(x)[1])

  return quantify(iobj.numeric_tuples(), f)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
