#!/usr/bin/env python

import collections
from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

import networkx as nx

YEAR = 2018
DAY = 25


rows = list(map(tuple, input_as_numeric_tuples(DAY, year=YEAR)))

def dfs(start=None, adjacent_fn=None, goal_fn=None):
  """
  >>> G = {\
    1: [2, 3, 6],\
    2: [1, 3, 4],\
    3: [1, 6, 2],\
    4: [2, 3, 5],\
    5: [4, 6],\
    6: [1, 3, 5],\
  }; dfs(1, lambda x: G[x], lambda x: x == 6)
  {1: None, 2: 1, 3: 1, 6: 1}
  """
  S = collections.deque()

  S.append(start)
  visited = set()
  pr = {start: None}

  while not len(S) == 0:
    v = S.pop()
    if v not in visited:
      visited.add(v)
      for child_state in adjacent_fn(v):
        if child_state not in pr:
          pr[child_state] = v
        if goal_fn(child_state):
          return pr
        S.append(child_state)
  assert set(pr.keys()) == visited
  return pr

def connected_components(nodes, adjacent_fn=None):
  """
  >>> connected_components(range(1, 11), lambda x: [y for y in range(1, 11) if y % 3 == x % 3])
  [(1, 10, 4, 7), (8, 2, 5), (9, 3, 6)]
  """
  components = []
  to_visit = set(nodes)

  while to_visit:
    start = to_visit.pop()
    pr = dfs(start, adjacent_fn, lambda x: False)
    to_visit -= set(pr.keys())
    components += [pr.keys()]
  return map(tuple, components)





def adj_list_from_fn(nodes, adj_fn):
  adj = {}
  for s in nodes:
    s = tuple(s)
    adj[s] = []
    for t in adj_fn(s):
      adj[s].append(tuple(t))
  return adj




def dist(pt1, pt2):
  return sum([abs(x-y) for (x,y) in zip(pt1, pt2)])

def adj_fn(pt):
  for other in rows:
    if dist(pt, other) <= 3:
      yield other


def part1(rows):
  x = adj_list_from_fn(rows, adj_fn)
  G = nx.Graph(x)

  #print(nx.info(G))

  return(len(list(nx.connected_components(G))))

  return


def part2(rows):
  cc = connected_components(rows, adj_fn)

  return len(list(cc))


import timeit
print(timeit.timeit('part1(rows)', globals=globals(), number=3))
print(timeit.timeit('part2(rows)', globals=globals(), number=3))
#print('P1', part1(rows))
#print('P2', part2(rows))
