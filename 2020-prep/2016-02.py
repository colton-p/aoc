from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2016
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

M = {
  'U': DIR.UP,
  'D': DIR.DOWN,
  'L': DIR.LEFT,
  'R': DIR.RIGHT,
}

def part1(rows, iobj):
  gs = """
  1 2 3
  4 5 6
  7 8 9
  """

  gs = """
  ..1
  .234
  56789
  .ABC
  ..D
"""
  G = Grid.from_string(gs.replace(' ' , ''))

  L = ''
  for steps in rows:
    pt = (0, 2)
    for step in steps:
      adj = vadd(pt, M[step]) 
      if G[adj] != '.':
        pt = adj
    L += str(G[pt])

  return L

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
