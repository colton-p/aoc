#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 20'
print '------'

rows = input_rows('20', test=False)

print 'row count:', len(rows)
print '------'


regex = "ENWWW(NEEE|SSE(EE|N))"

#["ENWWW", ["NEE", ["SSE", ["EE", "N"]]]]

def parse1(line):

  path = [{0: []}]

  while len(line):
    step = line.pop(0)

    if step == '^':
      path += [{0: []}]
    elif step in 'NEWS':
      l = path[-1]
      l[max(l.keys())] += step
    elif step == '|':
      l = path[-1]
      l[1+max(l.keys())] = []
    elif step == '(':
      l = path[-1]
      l[max(l.keys())] += parse1(line)
    elif step == ')':
      return path
      path += [{0: []}]
  return path




def f(steps):
  L = [ '' ]
  for v in steps:
    if isinstance(v, str):
      for (i,path) in enumerate(L):
        L[i] = path+v
    elif isinstance(v, dict):
      oL = [x for x in list(L)]
      L = [  ]
      for sub_steps in v.values():
        for (i,path) in enumerate(oL):
          for y in f(sub_steps):
            L += [path + y]
  return L


line = 'ENWWW(NEEE|SSE(EE|N))'
line = 'WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))'

line = rows[0][1:-1]

path = parse1(list(line))[0][0]

print len(line)
print len(path)

for p in path[:]:
  print len(f([p]))
exit()
all_paths = f(path[0])
#for path in all_paths:
#  print path
#print '----'

print 'all_paths', len(all_paths)

G = defaultdict(str)

STEPS = {
  'N': (0, -1),
  'S': (0, +1),
  'E': (+1, 0),
  'W': (-1, 0),
}

EDGES = set()
for path in all_paths:
  pos = (0, 0)
  for direction in path:
    dt = STEPS[direction]

    old_pos = pos
    pos = (pos[0] + dt[0], pos[1] + dt[1])
    edge = tuple(sorted([old_pos, pos]))
    EDGES.add( edge )


print 'edges', len(EDGES)
V = set(itertools.chain(*EDGES))
print 'v', len(V)


ADJ = {}
for v in V:
  ADJ[v] = [(y,1) for (x,y) in EDGES if x == v]
  ADJ[v] += [(y,1) for (y,x) in EDGES if x == v]

dist, prev = dijkstra(V, start=(0,0), adjacent_fn=lambda x: ADJ[x])

print '---'
print max(dist.iteritems(), key=lambda x:x[1])
