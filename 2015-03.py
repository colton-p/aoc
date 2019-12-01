#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

DAY = 3
YEAR = 2015

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(row, iobj):
  s = iobj.single_string()
  x = 0
  y = 0

  ss = set([0,0])

  for c in s:
    if c == '^': y+=1
    if c == 'v': y-=1
    if c == '<': x-=1
    if c == '>': x+=1

    ss.add( (x,y))

  return len(ss)


def part2(row, iobj):
  s = iobj.single_string()
  x = 0
  y = 0

  ss = set()
  ss.add ( (0,0))

  for (ix,c) in enumerate(s):
    if ix % 2 == 0:
      if c == '^': y-=1
      if c == 'v': y+=1
      if c == '<': x-=1
      if c == '>': x+=1

      ss.add( (x,y))

  x = 0
  y = 0
  for (ix,c) in enumerate(s):
    if ix % 2 == 1:
      if c == '^': y-=1
      if c == 'v': y+=1
      if c == '<': x-=1
      if c == '>': x+=1

      ss.add( (x,y))


  return len(ss)

print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
