from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rows = input_rows('input.txt')

def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

#grid = rows_to_grid(rows)
#rows = map(int, rows)

#count = count_with_predicate(rows, fff)
#print count

# c = 0
# for row in rows:

# print c
#with open('input.txt', 'r') as f:
#  rows = [line for line in f]

C = collections.defaultdict(int)
cond_func = {
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne,
}

rows = [row.split(' ') for row in rows]
print rows[0]

L = []
for (p0, v0, a0) in rows:
  p = p0[3:-2]
  p = map(int, p.split(','))

  v = v0[3:-2]
  v = map(int, v.split(','))

  a = a0[3:-1]
  a = map(int, a.split(','))


  L += [{"p": tuple(p), "v": tuple(v), "a": tuple(a)}]


POS = {}

def sim(ll):
  a0 = ll["a"]
  v0 = ll["v"]
  p0 = ll["p"]
  v1 = (v0[0] + a0[0], v0[1] + a0[1], v0[2] + a0[2])

  p1 = (v1[0] + p0[0], v1[1] + p0[1], v1[2] + p0[2])

  return {"p": tuple(p1), "v": tuple(v1), "a": tuple(a0)}

def pos(ll):
  return sum(map(abs,ll["p"]))
for (i, ll) in enumerate(L):
  POS[i] = pos(ll)


print POS[0]
print POS[1]
print POS[10]
print min(POS.items(), key=lambda x:x[1])

last = None
for i in range(10000):
  for ix in range(len(L)):
    if L[ix] is None:
      continue
    L[ix] = sim(L[ix])

  c = collections.Counter([ll["p"] for ll in L if ll])
  to_del = [p for (p, cnt) in c.iteritems() if cnt > 1]
  for ix in range(len(L)):
    if L[ix] is None:
      continue
    if L[ix]["p"] in to_del:
      L[ix] = None

  for ix in range(len(L)):
    if L[ix] is None:
      continue
    POS[ix] = pos(L[ix])


  mm = min(POS.items(), key=lambda x:x[1])[0]
  print i, len([x for x in L if x])
  if last != mm:
    last = mm
    print i, mm








#rows = [(int(x.strip()), int(y.strip())) for (x,y) in rows]

#ADJ = {}
#for (x, adjs) in rows:
#  ADJ[x] = [y.strip() for y in adjs]

#start = '0'
#adj_fn = lambda x: ADJ[x]
#goal_fn = lambda x: False

#row = split_rows(rows, sep=',')[0]
#rows = split_rows(rows, regex='([a-z]+) \((\d+)\)( -> )?(.*)?')

#L = []
#for row in rows:
#  L += []
#print max(L)

