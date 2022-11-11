from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2019
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):

  return quantify(iobj.int_list(), lambda x: x // 3 - 2)

def part2(rows, iobj):
  
  def f(x):
    s = 0

    while True:
      x = x // 3 - 2
      if x < 0:
        break
      s += x
    return s

  return quantify(iobj.int_list(), f)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
