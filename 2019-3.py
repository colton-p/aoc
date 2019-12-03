#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 3

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def step(i, pos):
  d = {
    'U': (0,1),
    'D': (0,-1),
    'L': (-1,0),
    'R': (1,0)
  }[i[0]]

  l = int(i[1:])

  seen = []
  for x in (range(l)):
    pos = tuple(vadd(pos, d))
    seen += [pos]

  return (seen, pos)


def part1(rows, iobj):
  p1 = rows[0].split(',')
  p2 = rows[1].split(',')

  #p1 = 'R8,U5,L5,D3'.split(',')
  #p2 = 'U7,R6,D4,L4'.split(',')

  seen1 = []
  seen2 = []

  pos1=(0,0)
  pos2=(0,0)

  for ix in range(len(p1)):
    s1 = p1[ix]
    s2 = p2[ix]

    (new1, pos1) = step(s1, pos1)
    (new2, pos2) = step(s2, pos2)

    seen1 = seen1 + new1
    seen2 = seen2 + new2


  ins = set(seen1) & set(seen2)

  closest = min(ins, key=lambda x: vdist1(x, (0,0)))

  #print(2+min([seen1.index(x) + seen2.index(x) for x in ins]))

  return vdist1(closest, (0,0))


def part2(rows, iobj):
  p1 = rows[0].split(',')
  p2 = rows[1].split(',')

  seen1 = []
  seen2 = []

  pos1=(0,0)
  pos2=(0,0)

  for ix in range(len(p1)):
    s1 = p1[ix]
    s2 = p2[ix]

    (new1, pos1) = step(s1, pos1)
    (new2, pos2) = step(s2, pos2)

    seen1 = seen1 + new1
    seen2 = seen2 + new2


  ins = set(seen1) & set(seen2)

  return (2+min([seen1.index(x) + seen2.index(x) for x in ins]))


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
