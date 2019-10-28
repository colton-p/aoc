#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op


def dd(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p2[1] - p1[1])

print 'Day 6'
print '------'

rows = input_rows('6.in')
print 'rows: ', len(rows)
print '--'

rows = [extract_numbers(i) for i in rows]

"""
rows = [
 [1, 1],
 [1, 6],
 [8, 3],
 [3, 4],
 [5, 5],
 [8, 9],
]
"""


X0 = min(rows, key=lambda x: x[0])[0]
X1 = max(rows, key=lambda x: x[0])[0]

Y0 = min(rows, key=lambda x: x[1])[1]
Y1 = max(rows, key=lambda x: x[1])[1]

print X0, Y0


D = defaultdict(list)
E = defaultdict(lambda: 999)
G = defaultdict(lambda: '.')
for x in range(X0-2, X1+1):
  for y in range(Y0-2, Y1+1):
    ll = sorted([(ix, pt, dd([x,y], pt)) for (ix, pt) in enumerate(rows)], key = lambda x:x[2])

    E[(x,y)] = sum([d for (_,_,d) in ll])
    if ll[0][2] == ll[1][2]:
      continue

    (ix, pt, dist) = ll[0]

    code = 'abcdefghijklmnopqrstuvwxyz01234567890!@#$%^&*()-_=+?/\,'[ix]


    G[(x,y)] = code
    if dist == 0:
      G[(x,y)] = G[(x,y)].upper()
    D[code] += [(x,y)]


skip = set()
for (x,y) in G:
  if x in [X0, X1] or y in [Y0, Y1]:
    skip.add(G[(x,y)])
print 'skip', skip

P1 = []
for k in set(D.keys()) - set(skip):
  P1 += [len(D[k])]
  print k, len(D[k])
print '----'
print 'A:', max(P1)
print '----'
print '----'

print sum([1 for v in E.values() if v < 10000])


