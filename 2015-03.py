#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

DAY = 3
YEAR = 2015

# TODO: how smart to make this?
rows = input_rows(DAY, year=YEAR)

(kind, rows, min_row, max_row, _x) = analyze_input(rows)
print("  Kind: %s" % kind)
print("n rows: %4d" % rows)
if min_row == max_row:
  print("n cols: %4d" % (max_row))
else:
  print("n cols: %4d-%4d" % (min_row, max_row))
print('.' * 16)
print('')

string = input_as_single_string(DAY, year=YEAR)

def part1(s):
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


def part2(s):
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

print('P1', part1(string))
print('P2', part2(string))
