#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 8'
print '------'

rows = input_rows('8', test=False)

row = rows[0]

print 'row count:', len(rows)
print '------'

L = extract_numbers(row)
print L
print len(L)


def f(ix):
  s = 0

  orig_ix = ix
  (n_child, n_meta) = L[ix], L[ix+1]

  ix += 2
  print 'child, meta:', (n_child, n_meta)
  child_weights = {}
  for i in range(n_child):
    (ix_delta, meta_size) = f(ix)
    ix += ix_delta
    #s += meta_size
    child_weights[i+1] = meta_size

  print child_weights
  if n_child == 0:
    for i in range(n_meta):
      print '-->', L[ix]
      s += L[ix]
      ix += 1
  else:
    for i in range(n_meta):
      print '*-->', L[ix], child_weights.get(L[ix], 0)
      s += child_weights.get(L[ix], 0)
      ix += 1

  return (ix - orig_ix, s)

print '----'
print f(0)[1]
