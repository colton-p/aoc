#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 7'
print '------'

rows = input_rows('7', test=False)

print 'row count:', len(rows)
print '------'

G = defaultdict(list)



req = defaultdict(list)
for row in rows:
  G[row[5]] += [row[36]]

  req[row[36]] += [row[5]]

print G
print req


to_visit = sorted(set(G.keys()) - set (itertools.chain(*G.values())))
path = []

while len(to_visit) != 0:
  parent = to_visit.pop(0)

  path += [parent]

  for child in G[parent]:
    if len(set(req[child]) - set(path)) > 0:
      continue
    if child in path:
      continue
    if child not in to_visit:
      to_visit += [child]

  to_visit = sorted(to_visit)

print ''.join(path)

print '----'

keys = set(G.keys()) | set(req.keys())

done = []

N_WORKERS = 5
OFFSET = 60
T = lambda x: ord(x) - ord('A') + 1 + OFFSET


avail = sorted([k for k in keys if 0 == len(set(req[k]) - set(done))])

WORKERS = [(None,0) for i in range(N_WORKERS)]

t = 0
for i in range(2000000):
  if set(done) == keys:
    break
  for w_ix in range(N_WORKERS):
    avail = sorted([k for k in keys if 0 == len(set(req[k]) - set(done)) and k not in done and k not in set([w[0] for w in WORKERS])])
    (job, left) = WORKERS[w_ix]
    if left == 0:
      if job is not None:
        done += [job]
        avail = sorted([k for k in keys if 0 == len(set(req[k]) - set(done)) and k not in done and k not in set([w[0] for w in WORKERS])])
      if len(avail):
        node = avail.pop(0)
        WORKERS[w_ix] = (node, T(node)-1)
      else:
        WORKERS[w_ix] = (None, 0)
    else:
      (job, left) = WORKERS[w_ix]
      WORKERS[w_ix] = (job, left - 1)
  print WORKERS,
  print done, avail,
  print ''
print i-1


