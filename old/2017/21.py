from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rules = input_rows('input.txt')


rules = [rule.split(' => ') for rule in rules]
rules = [(rows_to_grid(x.split('/')), rows_to_grid(y.split('/'))) for (x,y) in rules]

grid = rows_to_grid([".#.",
                     "..#",
                     "###"])


def match(pattern, rule):
  (key, value) = rule
  return set(key.iteritems()) == set(pattern.iteritems())

def transform_funcs2(N):
  e = lambda x,y: (x, y)
  a = lambda x,y: (y, N-x)
  b = lambda x,y: (x, N-y)

  a2 = lambda x,y: (N-x, N-y)
  a3 = lambda x,y: (N-y, x)

  ab = lambda x,y: (N-y, N-x)
  a2b = lambda x,y: (N-x, y)
  a3b = lambda x,y: (y, x)

  return [e,a,b,a2,a3,ab,a2b,a3b]


def transform_funcs(N):
  a = lambda x,y: (y, N-x)
  b = lambda x,y: (x, N-y)

  return [
    lambda x,y: (x,y),
    a,
    b,
    lambda x,y: a(*a(x,y)),
    lambda x,y: a(*a(*a(x,y))),
    lambda x,y: a(*b(x,y)),
    lambda x,y: a(*a(*b(x,y))),
    lambda x,y: a(*a(*a(*b(x,y))))
  ]


def transform(pattern):
  N = int(math.sqrt(len(pattern)))-1
  assert (N+1)*(N+1) == len(pattern)
  for func in transform_funcs(N):
    yield transform1(pattern, func)

def transform1(pattern, func):
  out = {}
  for (x,y),v in pattern.iteritems():
    out[func(x, y)] = v
  return out

def enhance(grid):
  for (ix,rule) in enumerate(rules):
    if any((match(tx, rule) for tx in transform(grid))):
      return rule[1]
  assert False

def split_grid(grid):
  N = int(math.sqrt(len(grid)))
  assert (N)*(N) == len(grid)

  if N % 2 == 0:
    k = 2
  elif N % 3 == 0:
    k = 3
  else:
    assert False, N

  xgrps = grouper(range(N), k)
  ygrps = grouper(range(N), k)

  for ((gx,xs),(gy,ys)) in itertools.product(enumerate(xgrps),enumerate(ygrps)):
    out = {}
    for ((ix, x),(iy, y)) in itertools.product(enumerate(xs),enumerate(ys)):
      out[(ix, iy)] = grid[(x,y)]
    yield (gx,gy), out


def enhance_all(grid):
  out = {}
  for ((gx, gy), subgrid) in split_grid(grid):
    N = int(math.sqrt(len(subgrid)))+1
    for ((x,y), v) in enhance(subgrid).items():
      out[(gx * N + x, gy * N + y)] = v
  return out

#grid
print len(grid)
print_grid(grid)
print ''

for i in enumerate(range(14)):
  grid = enhance_all(grid)
  print i, len(grid), len([v for v in grid.values() if v == '#'])
  #print_grid(grid)
  #print ''

