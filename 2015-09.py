#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

import networkx as nx

from util import *

YEAR = 2015
DAY = 9

# TODO: how smart to make this?
rows = input_rows(DAY, year=YEAR)

(kind, rows, max_row, min_row, _x) = analyze_input(rows)
print("  Kind: %s" % kind)
print("n rows: %4d" % rows)
if min_row == max_row:
  print("n cols: %4d" % (max_row))
else:
  print("n cols: %d-%d" % (min_row, max_row))
print('.' * 16)
print('')


rows = input_as_tuples(DAY, year=YEAR)

# TODO: tuples to adj??
adj = {}
for (a, _x, b, _y, dd) in rows:
  adj[(a,b)] = dd
  adj[(b,a)] = dd


G = nx.Graph()
for k,v in adj.items():
  G.add_edge(k[0], k[1], weight=v)

print(nx.info(G))
print(nx.get_edge_attributes(G, 'weight'))
def part1(G):

  v =0

  for a in G.nodes():
    for b in G.nodes():
      if a >= b:
        continue
      for p in nx.all_simple_paths(G, a, b):
        if len(p) != len(G.nodes()):
          continue

        x = ( sum([G[e[0]][e[1]]['weight'] for e in pairwise(p)]))
        if x > v:
          v = x

  return v


def part2(s):

  return


print('P1', part1(G))
print('P2', part2(rows))
