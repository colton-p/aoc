#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import random
import operator as op

print 'Day 23'
print '------'

rows = input_rows('23', test=False)

print 'row count:', len(rows)
print '------'


def dist(pt1, pt2):
  return sum([abs(x-y) for (x,y) in zip(pt1,pt2)])

pts = []
for row in rows:
  (x,y,z,r) = extract_numbers(row)
  pts += [((x,y,z), r)]

G = defaultdict(int)

def f(src):
  c = 0
  for (pt,r) in pts:
    if dist(pt, src) <= r:
      c+=1
  return c


def adj(pt):
  L = []
  (x,y,z) = pt
  for step in [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    for d in [-1, 1]:
      L += [ (x + d*step, y, z), (x, y+d*step, z) ,(x,y,z+d*step)]
  return sorted(L, key=f, reverse=True)

opt = (22491503, 27851295, 28344918)

print len(pts)
print sum(opt)
print f(opt)
print f((21855350, 28874177, 27958189))
exit()

pt = (0,0,0)
best = pt

for i in range(10000):
  print pt, f(pt), '|', best, f(best)

  if f(pt) > f(best):
    best = pt

  a = adj(pt)

  if f(a[0]) > f(pt):
    pt = a[0]
  else:
    pt = random.choice(a)






