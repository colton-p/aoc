#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
rows = list(iobj.rows)

def bfs(start=None, adjacent_fn=None, goal_fn=None):
  open_set = collections.deque()
  closed_set = set()

  # a dictionary to maintain meta information (used for path formation)
  meta = dict()  # key -> (parent state, action to reach child)

  # initialize
  meta[start] = (None)
  open_set.append(start)

  while len(open_set) > 0:
    parent_state = open_set.popleft()

    if goal_fn and goal_fn(parent_state):
      return construct_path(parent_state, meta)

    for child_state in adjacent_fn(parent_state):

      if child_state in closed_set:
        continue


      if child_state not in open_set:
        meta[child_state] = parent_state
        open_set.append(child_state)

    closed_set.add(parent_state)

  return meta

def construct_path(state, meta):
  path = []

  while state in meta:
    path.append(state)
    state = meta[state]

  return list(reversed(path))

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

def dijkstra(start=None, adjacent_fn=None):
  seen = set()
  Q = set()

  dist = defaultdict(lambda: 999999)
  prev = defaultdict(lambda: None)

  Q.add(start)

  dist[start] = 0

  while len(Q) != 0:
    u = min(Q, key=lambda v: dist[v])

    Q.remove(u)
    seen.add(u)

    print(len(seen), len(max(seen, key=lambda v: len(v[1]))), len(Q))

    for (v, weight) in adjacent_fn(u):
      if v in seen:
        continue
      alt = dist[u] + weight
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
      Q.add(v)

  return dist, prev

from heapdict import heapdict
def dijkstra2(start=None, adjacent_fn=None):
  seen = set()
  Q = heapdict()

  lvl = 0

  dist = defaultdict(lambda: 999999)
  prev = defaultdict(lambda: None)

  Q[start] = 0
  dist[start] = 0

  while len(Q) != 0:
    u = Q.popitem()[0]

    seen.add(u)

    this_lvl = len(u[1])
    if this_lvl > lvl:
      print(len(seen), this_lvl, len(Q))
      lvl = this_lvl

    for (v, weight) in adjacent_fn(u):
      if v in seen:
        continue
      alt = dist[u] + weight
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
      Q[v] = dist[v]

  return dist, prev


def rows_to_grid_default(rows, default=None):
  DD = rows_to_grid(rows)

  D = defaultdict(lambda: default)
  for k,v in DD.items():
    D[k] = v
  return D

def distances_to_keys(D, source_sym, keys):
  all_keys = frozenset([v for v in D.values() if v in 'abcdefghijklmnopqrstuvwxyz'])
  all_doors = frozenset([v for v in D.values() if v in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

  (source,) = [k for k in D if D[k] == source_sym]

  def adj_fn_builder(keys):
    def adj_fn(pt):
      if D[pt] in all_keys and D[pt] not in keys:
        return []

      for adj in rect_adj(pt):
        if D[adj] in '.@0123':
          yield adj
        elif D[adj] in all_keys:
          yield adj
          #if D[adj] in keys:
          #  yield (adj, keys)

          #new_keys = frozenset(keys) | frozenset([D[adj]])
          #yield (adj, new_keys, dist+1)
        elif D[adj] in all_doors:
          if D[adj].lower() in keys:
            yield adj
    return adj_fn


  ret = {}
  pr = bfs(source, adjacent_fn=adj_fn_builder(keys),goal_fn=None)
  for (child,parent) in pr.items():
    if D[child] in all_keys and D[child] not in keys:
      ret[D[child]] = len(construct_path(child, pr))-1
  return ret

def part1(rows, iobj):
  D = rows_to_grid_default(rows, default='#')

  (source,) = [k for k in D if D[k] == '@']

  all_keys = frozenset([v for v in D.values() if v in 'abcdefghijklmnopqrstuvwxyz'])

  def adj_fn(node):
    (last, keys) = node

    dist = distances_to_keys(D, last, keys)

    for k,v in dist.items():
      yield ((k, frozenset(keys) | frozenset(k)), v)


  dist, prev = dijkstra(start=('@', frozenset()), adjacent_fn=adj_fn)

  for k in dist:
    if k[1] == all_keys:
      print(k, dist[k])

  return

  """
  G = nx.DiGraph()
  for k in D:
    G.add_node(k)
  for s in D:
    for t in rect_adj(s):
      if D[s] in '@.' and D[t] in '@.':
        G.add_edge(s,t)
        G.add_edge(t,s)
      if D[s] in '@.' and D[t] not in '#':
        G.add_edge(s,t)

  (SRC,) = [k for k in D if D[k] == '@']
  print(SRC)
  print(nx.info(G))

  for tgt in [k for k in D if D[k] in 'abcdefghijklmnopqrstuvwxyz']:
    print(tgt, nx.has_path(G, SRC, tgt))
  #print(t[D[k] for k in nx.shortest_path(G, SRC, keya)])

  return
  """

def part2(rows, iobj):
  DD = rows_to_grid(rows)

  D = defaultdict(lambda: '#')
  for k,v in DD.items():
    D[k] = v


  (SRC,) = [k for k in D if D[k] == '@']
  for k in rect_adj(SRC, diag=True):
    if vdist1(SRC, k) == 1:
      D[k] = '#'
    elif vdist1(SRC, k) == 2:
      D[k] = '@'
  D[SRC] = '#'

  for (ix, k) in enumerate([k for k in D if D[k] == '@']):
    D[k] = str(ix)


  srcs = ('0', '1', '2', '3')

  start = (srcs, frozenset())
  def adj_fn(node):
    (lasts, keys) = node

    for (ix,last) in enumerate(lasts):
      dist = distances_to_keys(D, last, keys)

      for k,v in dist.items():
        new_pos = list(lasts)
        new_pos[ix] = k
        new_pos = tuple(new_pos)

        yield ((new_pos, frozenset(keys) | frozenset(k)), v)


  #for x in adj_fn(start):
  #  print(x)
  dist, prev = dijkstra2(start=start, adjacent_fn=adj_fn)

  all_keys = frozenset([v for v in D.values() if v in 'abcdefghijklmnopqrstuvwxyz'])

  for k in dist:
    if k[1] == all_keys:
      print(k, dist[k])



  return


#print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
