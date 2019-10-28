#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 12'
print '------'

rows = input_rows('12', test=False)

print 'row count:', len(rows)
print '------'

init = rows[0][15:]

A = defaultdict(lambda: '.')
for (ix, x) in enumerate(init):
  if x == '#':
    A[ix] = x
print A

def pp(A):
  for ix in range(min(A.keys())-2, max(A.keys())+2):
    print A[ix],
  print ''

rules = defaultdict(lambda : '.')
for r in rows[2:]:
  (k,v) = r.split(' => ')
  rules[k] = v

print rules
def evolve(A):
  B = defaultdict(lambda : '.')
  for ix in range(min(A.keys())-2, max(A.keys())+2):
    k = A[ix-2] + A[ix-1] + A[ix] + A[ix + 1] + A[ix + 2]
    if k in rules:
      v = rules[k]
      B[ix] = v
    else:
      pass
      #B[ix] = A[ix]
  return B

print ''
pp(A)
for i in range(200):
  A = evolve(A)
  print i, sum([k for k in A.keys() if A[k] == '#'])




