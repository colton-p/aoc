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

def f(L):
  s = 0
  n_child = L.pop(0)
  n_meta = L.pop(0)

  for i in range(n_child):
    s += f(L)

  for i in range(n_meta):
    s += L.pop(0)
  return s

def g(L):
  s = 0
  n_child = L.pop(0)
  n_meta = L.pop(0)

  child_weights = {}
  for i in range(n_child):
    child_weights[i+1] = g(L)

  for i in range(n_meta):
    val = L.pop(0)
    if n_child == 0:
      s += val
    else:
      s += child_weights.get(val, 0)
  return s

print f(list(L))
print g(list(L))
