#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 11'
print '------'

rows = input_rows('11', test=False)
print rows

serial_no = int(rows[0])

print 'row count:', len(rows)
print '------'


def f(x,y):
  rack_id = x + 10
  power = rack_id * y
  power += serial_no
  power *= rack_id

  power = (power / 100) % 10
  return power - 5


G = defaultdict(int)

for x in range(1, 301):
  for y in range(1, 301):
    G[(x,y)] = f(x,y)


def adj(x, y, s):
  for i in range(s):
    for j in range(s):
      yield (x+i, y+j)


print list(adj(0, 0, 3))
print len(list(adj(0, 0, 3)))

D = {}
for size in range(1, 301):
  for x in range(1, 301):
    for y in range(1, 301):
      D[(x,y, size)] = sum([G[(i,j)] for (i,j) in adj(x,y, size)])

  print size, max(D.iteritems(),key=lambda x: x[1])

