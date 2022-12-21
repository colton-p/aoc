from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

import util.grid2 as grid2

YEAR = 2022
DAY = 10

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def go(rows):
  X = 1
  pc = 1

  for row in rows:
    if row == 'noop':
      yield (pc, X)
      pc += 1
    else:
      (op, val) = row.split(' ')
      val = int(val)
      assert op == 'addx'
      for i in range(2):
        yield (pc, X)
        pc += 1
      
      X += val




def part1(rows, iobj):

  s = 0
  for (pc, x) in go(rows):
    if pc % 40 == 20:
      s += (pc * x)

  return s

def part2(rows, iobj):

  G = {}
  for (pc, x) in go(rows):
    col = (pc-1) % 40
    row = ((pc-1) // 40)

    G[(col, row)] = '.'
    if col in (x-1, x, x+1):
      G[(col, row)] = '#'

  GG = grid2.FixedGrid(G)

  print(GG.to_s(cell_size=2))

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
