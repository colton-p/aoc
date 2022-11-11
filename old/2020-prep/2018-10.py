#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 10

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def draw(pos):
  G = Grid.from_dict( {p: '#' for p in pos} )

  return (G, G.max_y() - G.min_y())

def evolve(pos, vel):
  return [ vadd(p, v) for (p,v) in zip(pos, vel) ]

def part1(rows, iobj):

  pos = [(x,y) for (x, y, _, _) in iobj.numeric_tuples()]
  vel = [(x,y) for (_, _, x, y) in iobj.numeric_tuples()]

  v = 10000
  c = 0
  while v > 12:
    pos = evolve(pos, vel)
    c +=1
    (G, v) = draw(pos)

  G.print()
  return c


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
