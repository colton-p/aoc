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
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def bfs(start=None, adjacent_fn=None, goal_fn=None, passable_fn=lambda x: True):

  LVL = 0
  ii = 0

  open_set = collections.deque()
  closed_set = set()

  # a dictionary to maintain meta information (used for path formation)
  meta = dict()  # key -> (parent state, action to reach child)

  # initialize
  meta[start] = (None)
  open_set.append(start)

  while len(open_set) > 0:
    parent_state = open_set.popleft()
    ii += 1

    if parent_state[-1] > LVL:
      print("%4d | keys=%2d | done=%6d queue=%6d iters=%8d" % (parent_state[-1], len(parent_state[1]), len(closed_set), len(open_set), ii))
      LVL = parent_state[-1]

    if goal_fn(parent_state):
      return construct_path(parent_state, meta)

    for child_state in adjacent_fn(parent_state):

      if child_state in closed_set:
        continue


      if child_state not in open_set:
        meta[child_state] = parent_state
        open_set.append(child_state)

    closed_set.add(parent_state)

def construct_path(state, meta):
  path = []

  while state in meta:
    path.append(state)
    state = meta[state]

  return list(reversed(path))




def part1(rows, iobj):
  DD = rows_to_grid(rows)

  D = defaultdict(lambda: '#')
  for k,v in DD.items():
    D[k] = v

  print_grid(D)

  (SRC,) = [k for k in D if D[k] == '@']
  D[SRC] = '.'


  start = (SRC, frozenset(), 0)

  all_keys = frozenset([v for v in D.values() if v in 'abcdefghijklmnopqrstuvwxyz'])
  all_doors = frozenset([v for v in D.values() if v in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
  print(all_keys)

  def adj_fn(state):
    (pt, keys, dist) = state

    for adj in rect_adj(pt):
      if D[adj] == '.':
        yield (adj, keys, dist+1)
      elif D[adj] in all_keys:
        yield (adj, frozenset(keys | frozenset([D[adj]])), dist+1)
      elif D[adj] in all_doors:
        if D[adj].lower() in keys:
          yield (adj, keys,dist+1)


  pr = bfs(start, adjacent_fn=adj_fn,goal_fn=lambda state: (state[1]) == (all_keys))
  for x in pr:
    print(x)
  print(len(pr)-1)

  return

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


def part2(rows, iobj):
  DD = rows_to_grid(rows)

  D = defaultdict(lambda: '#')
  for k,v in DD.items():
    D[k] = v

  print_grid(D)

  (SRC,) = [k for k in D if D[k] == '@']
  for k in rect_adj(SRC, diag=True):
    if vdist1(SRC, k) == 1:
      D[k] = '#'
    elif vdist1(SRC, k) == 2:
      D[k] = '@'
  D[SRC] = '#'

  srcs = tuple(k for k in D if D[k] == '@')

  start = (srcs, frozenset(), 0)

  all_keys = frozenset([v for v in D.values() if v in 'abcdefghijklmnopqrstuvwxyz'])
  all_doors = frozenset([v for v in D.values() if v in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
  print(all_keys)

  def adj_fn(state):
    (pts, keys, dist) = state

    for (pt_ix, pt) in enumerate(pts):
      for adj in rect_adj(pt):
        new_pts = list(pts)
        new_pts[pt_ix] = adj
        new_pts = tuple(new_pts)


        if D[adj] == '.':
          yield (new_pts, keys, dist+1)
        elif D[adj] in all_keys:
          yield (new_pts, frozenset(keys | frozenset([D[adj]])), dist+1)
        elif D[adj] in all_doors:
          if D[adj].lower() in keys:
            yield (new_pts, keys,dist+1)


  pr = bfs(start, adjacent_fn=adj_fn,goal_fn=lambda state: (state[1]) == (all_keys))
  for x in pr:
    print(x)
  print(len(pr)-1)


  return


# print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
