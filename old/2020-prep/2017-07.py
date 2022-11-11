#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from networkx import nx

from util import *

YEAR = 2017
DAY = 7

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def build(rows):
  G = nx.DiGraph()

  for row in rows:
    node = row.split(' ')[0]
    (weight,) = ints(row)
    G.add_node(node, weight=weight)
    if '->' in row:
      right = row.split(' -> ')[1]
      for x in right.split(', '):
        G.add_edge(node, x.strip())
    
  return G

def part1(rows, iobj):
  G = build(rows)

  for (x, d) in G.in_degree():
    if d == 0:
      return x

  return


def part2(rows, iobj):
  G = build(rows)

  for n in reversed(list(nx.topological_sort(G))):
    G.nodes[n]['value'] = sum(G.nodes[c]['value'] for c in G[n] ) + G.nodes[n]['weight']
  
  def val(n):
    return G.nodes[n]['value']

  for n in nx.topological_sort(G):
    parents = list(G.predecessors(n))
    if not parents:
      continue
    (parent,) = parents

    tgt = Counter(val(sib) for sib in G[parent])
    tgt = detect(tgt, lambda x: tgt[x] > 1)

    all_child_same = len(set(val(c) for c in G[n])) == 1
    if tgt != val(n) and all_child_same:

      return tgt - val(n) + G.nodes[n]['weight']


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
