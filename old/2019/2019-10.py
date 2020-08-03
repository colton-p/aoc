#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 10

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def ray(G, pt, slope):
  c = 0
  x = pt
  while True:
    x = tuple(vadd(x, slope))

    if x not in G:
      break
    if G[x] == '#':
      G[x] = '.' # boom
      return [x]
    if G[x] == '.':
      continue

  return []


def slopes():
  s = []
  for dx in range(-48, 48):
    for dy in range(-48, 48):
      s += [(dx, dy)]

  return sorted(s, key=lambda x: -math.atan2(x[0], x[1]))


def visible(G, pt):
  c = []
  for (dx,dy) in slopes():
    if dx == 0 and dy == 0:
      continue
    if gcd(abs(dx), abs(dy)) != 1:
      continue
    if dx == 0 and abs(dy) != 1:
      continue
    if dy == 0 and abs(dx) != 1:
      continue

    c += ray(G, pt, (dx, dy))

  return c


def part1(rows, iobj):
  ll = iobj.tuples()
  G = rows_to_grid(rows)


  PT = (20, 21)

  kills = visible(G, PT)
  return kills[199]

  #pt_opt = max([pt for pt in G.keys() if G[pt] == '#'], key=lambda x: len(visible(G, x)))

  #return (pt_opt, len(visible(G,pt_opt)))


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
