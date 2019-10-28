from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

#rows = input_rows('input.txt')

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
with open('input.txt', 'r') as f:
  rows = [line for line in f]

C = collections.defaultdict(int)
cond_func = {
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne,
}


def adj(G, pt):
  for nn in rect_adj(pt):
    if G.get(nn, ' ').strip() == '':
      continue
    if nn[0] < 0 or nn[1] < 0:
      continue

    if G[nn] == '-' and nn[1] != pt[1]:
      continue
    elif G[nn] == '|' and nn[0] != pt[0]:
      continue
    else:
      yield nn


#rows = [row.split(': ') for row in rows]
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

G = rows_to_grid(rows)

pt = (1,0)
#pt = (5,0)
dd = (0, 1)



#print list(adj(G, (167, 89)))
L = [pt]


while True:
  next_pt = (pt[0] + dd[0], pt[1] + dd[1])

  if G[pt] != '+' and G[next_pt] != ' ':
    L += [next_pt]
    pt = next_pt
  else:
    adjs = set(adj(G, pt)) - set(L[-5:])
    if len(adjs) != 1:
      print [G[x] for x in L[-3:]]
      print [x for x in L[-3:]]
      print dd, pt, next_pt, set(adj(G, pt)), 
      break

    next_pt = list(adjs)[0]
    dd = (next_pt[0] - pt[0], next_pt[1] - pt[1])
    L += [next_pt]
    pt = next_pt

print ''
for x in L:
  if G[x] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print G[x]
print ''
for (i,x) in enumerate(L):
  print i+1, x, G[x]

print len(L)
