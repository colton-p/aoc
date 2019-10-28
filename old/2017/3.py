from util import *

import collections
import itertools
import re


#rows = split_rows(rows, sep='\t')
#count = count_with_predicate(rows, lambda x: len(x) > 1)

KEY = 368078

def rect_adj(s):
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      if (i,j) != (0,0):
        yield (s[0]+i, s[1]+j)


def adj_val(s):
  v = 0
  for t in rect_adj(s):
    v += E.get(t, 0)
  if v > KEY:
    print v
    raise v
  return v


direction  = {
  0: (1, 0),
  1: (0, 1),
  2: (-1, 0),
  3: (0, -1),
}


def pt_add(a,b):
  (x1, y1) = a
  (x2, y2) = b
  return (x1+x2,y1+y2)

D = {}
E = {}
D[1] = (0,0)
E[(0,0)] = 1

s = 1

dd = 0
n = 2
for side in range(1, 700):
  for i in range(side):
    v = pt_add(D[n-1], direction[dd])
    D[n] = v
    E[v] = adj_val(v)
    n += 1

  dd += 1
  dd %= 4
  for i in range(side):
    v = pt_add(D[n-1], direction[dd])
    D[n] = v
    E[v] = adj_val(v)
    n += 1
  dd += 1
  dd %= 4


#print D[KEY]

#print sum(D[KEY])
