#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 10'
print '------'

rows = input_rows('10', test=False)

rows = [extract_numbers(r) for r in rows]

def f(x, y, vx, vy):
  return (x+vx, y+vy, vx, vy)

def g(rows):
  a = max(rows, key=lambda x: x[0])[0]
  b = max(rows, key=lambda x: x[1])[1]
  c = min(rows, key=lambda x: x[0])[0]
  d = min(rows, key=lambda x: x[1])[1]
  return (abs(c-a), abs(d-b))


for i in range(12000):
  rows = [f(*row) for row in rows]
  if g(rows)[1] < 10:
    break

grid = defaultdict(lambda: '.')
for (x,y,vx,vy) in rows:
  grid[(y,x)] = '#'

print_grid(grid)
print i+1

