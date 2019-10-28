#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 13'
print '------'

rows = input_rows('13', strip=False, test=False)

print 'row count:', len(rows)
print '------'

track = defaultdict(lambda : None)

carts = []

for (y, row) in enumerate(rows):
  for (x, val) in enumerate(row):
    if val != ' ':
      track[(x,y)] = val
    if val == 'v' or val == '^':
      track[(x,y)] = '|'
    if val == '>' or val == '<':
      track[(x,y)] = '-'
    if val in ['>', '<', '^', 'v']:

      if val == '>':
        dir = (1,0)
      elif val == '<':
        dir = (-1,0)
      elif val == '^':
        dir = (0,-1)
      elif val == 'v':
        dir = (0,1)

      carts += [((x,y), dir, 0)]

print carts

for iter_ix in range(20000):
  carts = sorted([x for x in carts if x[0]], key=lambda x: (x[0][1], x[0][0]))
  if len(carts) == 1:
    print '!!!'
    print carts
    exit()
  print iter_ix, len(carts)
  for ix in range(len(carts)):
    (pt, dir, mem) = carts[ix]

    if pt is None:
      continue

    rail = track[pt]

    new_mem = mem
    if rail == '-' or rail == '|':
      new_dir = dir
    elif rail == '/':
      new_dir = (-dir[1], -dir[0])
    elif rail == '\\':
      new_dir = (dir[1], dir[0])
    elif rail == '+':
      if mem == 0:
        new_dir = (dir[1], -dir[0])
      elif mem == 1:
        new_dir = dir
      elif mem == 2:
        new_dir = (-dir[1], dir[0])
      new_mem = (mem+1) % 3

    new_pt = (pt[0] + new_dir[0], pt[1] + new_dir[1])

    if track[new_pt] is None:
      print pt, new_pt
      print track[pt]
      print track[new_pt]
      print dir, new_dir


    assert track[new_pt] is not None

    if new_pt in [xx for (xx, _dir, _mem) in carts]:
      carts[ix] = (None, None, None)
      for (ii, (_pt, _dir, _mem)) in enumerate(carts):
        if new_pt == _pt:
          carts[ii] = (None, None, None)
          print ii, 'x', ix



    else:
      carts[ix] = (new_pt, new_dir, new_mem)


print carts
