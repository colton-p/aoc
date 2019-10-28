#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 25'
print '------'

rows = input_rows('25', test=False)

print 'row count:', len(rows)
print '------'


def dist(pt1, pt2):
  return sum([abs(x-y) for (x,y) in zip(pt1, pt2)])

pts = [tuple(extract_numbers(row)) for row in rows]

def adj(pt):
  for other in pts:
    if dist(pt, other) <= 3:
      yield other

cc = connected_components(pts, adj)

print len(cc)
