from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rows = input_rows('12.in')

rows = [row.split(' <-> ') for row in rows]
rows = [(x.strip(), y.split(',')) for (x,y) in rows]

ADJ = {}
for (x, adjs) in rows:
  ADJ[x] = [y.strip() for y in adjs]

start = '0'
adj_fn = lambda x: ADJ[x]
goal_fn = lambda x: False

pr = dfs(start, adj_fn, goal_fn)
print 'Part 1: ', len(pr)


###

c = 0
to_visit = set(ADJ.keys())
while to_visit:
  start = to_visit.pop()
  pr = dfs(start, adj_fn, goal_fn)
  to_visit = to_visit - set(pr.keys())
  c += 1

cc = connected_components(ADJ.keys(), adj_fn)

print 'Part 2: ', c
print 'Part 2: ', len(cc)


