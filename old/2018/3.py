#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

rows = input_rows('3.in')
print len(rows)


C = defaultdict(int)
D = defaultdict(list)

rows = [map(int, row) for row in split_rows(rows, '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')]
print rows[0]
for (ii, x, y, w, h) in rows:
  for i in range(x, x+w):
    for j in range(y, y+h):
      C[i, j] += 1
      D[i, j] += [ii]

for (ii, x, y, w, h) in rows:
  overlap = False
  for i in range(x, x+w):
    for j in range(y, y+h):
      if C[i,j] > 1:
        overlap = True
  if not overlap:
    print ii



print(sum([1 for i in C.values() if i > 1]))

# L = []
# for row in rows:
#   L += [f(row)]


