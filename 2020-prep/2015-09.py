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

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.pp_analyze()
rows = list(iobj.rows)

def parse(iobj):
  rows = iobj.tuples()

  adj = {}
  for (a, _x, b, _y, dd) in rows:
    adj[(a,b)] = dd
    adj[(b,a)] = dd

  G = nx.Graph()
  for k,v in adj.items():
    G.add_edge(k[0], k[1], w=v)

  return G


def part1(rows, iobj):
  G = parse(iobj)
  paths = itertools.permutations(G.nodes())

  return min(path_weight(G, path) for path in paths)

def part2(rows, iobj):
  G = parse(iobj)
  paths = itertools.permutations(G.nodes())

  return max(path_weight(G, path) for path in paths)


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
