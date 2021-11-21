from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 12

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part2(rows, iobj):

  pos = (0, 0)
  way = (10, -1)

  for line in rows:
    op = line[0]
    val = int(line[1:])

    if op  == 'N':
      way = vadd(way, vscale(DIR.NORTH, val))
    elif op == 'S':
      way = vadd(way, vscale(DIR.SOUTH, val))
    elif op == 'E':
      way = vadd(way, vscale(DIR.EAST, val))
    elif op == 'W':
      way = vadd(way, vscale(DIR.WEST, val))
    elif op == 'L':
      way = tuple(map(int, map(round,rotate_n_degrees(way, -val))))
    elif op == 'R':
      way = tuple(map(int, map(round,rotate_n_degrees(way, val))))
    elif op == 'F':
      pos = vadd(pos, vscale(way, val))

  return sum(map(abs,pos))

def part1(rows, iobj):
  pos = (0, 0)
  dir = DIR.EAST

  for line in rows:
    op = line[0]
    val = int(line[1:])

    if op  == 'N':
      pos = vadd(pos, vscale(DIR.NORTH, val))
    elif op == 'S':
      pos = vadd(pos, vscale(DIR.SOUTH, val))
    elif op == 'E':
      pos = vadd(pos, vscale(DIR.EAST, val))
    elif op == 'W':
      pos = vadd(pos, vscale(DIR.WEST, val))
    elif op == 'L':
      dir = tuple(map(int, map(round,rotate_n_degrees(dir, -val))))
    elif op == 'R':
      dir = tuple(map(int, map(round,rotate_n_degrees(dir, val))))
    elif op == 'F':
      pos = vadd(pos, vscale(dir, val))

  return sum(map(abs,pos))

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
