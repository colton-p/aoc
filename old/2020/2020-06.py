from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 6

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):
  pp = []

  p = ''
  for row in rows:
    if row:
      p += row + ' '
    else:
      pp += [ p ]
      p = ''
  else:
      pp += [ p ]
  
  def f(grp):
    grp = grp.split(' ')
    s = set(its.chain(*grp))

    return len(s)

  return quantify(pp, f)


def part2(rows, iobj):
  pp = iobj.line_delimited()

  import functools
  def f(grp):
    g = [set(x) for x in grp]
    return len(g[0].intersection(*g[1:]))

  return quantify(pp, f)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
