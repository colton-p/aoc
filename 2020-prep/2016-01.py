from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2016
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):
  pos = (0, 0)
  dir = DIR.NORTH
  for x in iobj.single_string().split(', '):
    d = x[0]
    v = int(x[1:])
    if d == 'L':
      dir = turn_left(dir)
    else:
      dir = turn_right(dir)
    pos = vadd(pos, vscale(dir, v))

  return sum(pos)

def part2(rows, iobj):
  def f():
    pos = (0, 0)
    dir = DIR.NORTH
    for x in iobj.word_tuples()[0]:
      d = x[0]
      v = int(x[1:])
      if d == 'L':
        dir = turn_left(dir)
      else:
        dir = turn_right(dir)
      for i in range(v):
        pos = vadd(pos, dir)
        yield pos

  return sum(detect_cycle_it(f())['s0'])

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
