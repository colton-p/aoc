#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 18'
print '------'

rows = input_rows('18', test=False)

print 'row count:', len(rows)
print '------'

G = {}

for (y,row) in enumerate(rows):
  for (x, val) in enumerate(row):
    G[(x,y)] = val


def adj((x,y), diag=True):
  return list(rect_adj_bounds((x,y), 0, 49, 0, 49, diag=True))


old_G = dict(G)
new_G = dict(G)

for ix in range(1000):
  old_G = dict(new_G)
  new_G = dict()

  for (x,y) in old_G.keys():
    if old_G[(x,y)] == '.':
      if len([old_G[(i,j)] for (i,j) in adj((x,y), diag=True) if old_G[(i,j)] == '|']) >= 3:
        new_G[(x,y)] = '|'
      else:
        new_G[(x,y)] = old_G[(x,y)]
    if old_G[(x,y)] == '|':
      if len([old_G[(i,j)] for (i,j) in adj((x,y), diag=True) if old_G[(i,j)] == '#']) >= 3:
        new_G[(x,y)] = '#'
      else:
        new_G[(x,y)] = old_G[(x,y)]
    if old_G[(x,y)] == '#':
      if len([old_G[(i,j)] for (i,j) in adj((x,y), diag=True) if old_G[(i,j)] == '#']) >= 1 and len([old_G[(i,j)] for (i,j) in adj((x,y), diag=True) if old_G[(i,j)] == '|']) >= 1:
        new_G[(x,y)] = '#'
      else:
        new_G[(x,y)] = '.'

  a = len([v for v in new_G.values() if v == '|'])
  b = len([v for v in new_G.values() if v == '#'])
  print ix, a*b
