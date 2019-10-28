#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
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
  return (c, -sum(src))

def adj(pt):
  (x,y,z) = pt
  for (dx,dy,dz) in itertools.product(*[ [-1,0,1] ]*3):
    yield (x+dx, y+dy, z+dz)

import random
pt = (22491502, 27851295, 28344918)
print f(pt)

best = pt
for i in range(10000):
  #a = list(adj(pt))
  #random.shuffle(a)
  new_pt = max(adj(pt), key=f)
  if f(new_pt) < f(pt):
    (x,y,z) = pt
    new_pt = (x+random.randint(-10,10), y+random.randint(-10,10), z+random.randint(-10,10))
  pt = new_pt

  if f(pt) > f(best):
    print 'NEW BEST'
    print f(best), f(pt)
    best = pt
    print ''

  #print pt, f(pt)
