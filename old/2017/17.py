from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator


def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

#grid = rows_to_grid(rows)
#rows = map(int, rows)

#count = count_with_predicate(rows, fff)
#print count

# c = 0
# for row in rows:
#  
# print c

C = collections.defaultdict(int)
cond_func = {
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne,
}

#rows = [(int(x.strip()), int(y.strip())) for (x,y) in rows]


#rows = [row.split(': ') for row in rows]
#ADJ = {}
#for (x, adjs) in rows:
#  ADJ[x] = [y.strip() for y in adjs]

#start = '0'
#adj_fn = lambda x: ADJ[x]
#goal_fn = lambda x: False

#row = split_rows(rows, sep=',')[0]

key = 369

def ins(L, i, x):
  return L[:i+1] + [x] + L[i+1:]


L = [0]
pos = 0

D = {}

"""
for i in range(1, 10):
  print i, len(L)
  pos = (pos + key) % len(L)
  L = ins(L, pos, i)
  pos += 1
  ix = L.index(0)

  goal = L[ix:ix+2][1]
  if goal not in D:
    print ix
    D[goal] = i

for k,v in sorted(D.iteritems()):
  print k, v
"""

for i in range(1, 50*1000*1000):
  if i % 10**6 == 0:
    print i
  pos = (pos + key) % (i)
  if pos == 0:
    print i
  pos += 1
