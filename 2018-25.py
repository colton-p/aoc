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

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.pp_analyze()
rows = list(iobj.rows)

def adj_list_from_fn(nodes, adj_fn):
  adj = {}
  for s in nodes:
    s = tuple(s)
    adj[s] = []
    for t in adj_fn(nodes, s):
      adj[s].append(tuple(t))
  return adj

def adj_fn(nodes, pt):
  for other in nodes:
    if vdist1(pt, other) <= 3:
      yield other

def part1(rows, iobj):
  pts = iobj.numeric_tuples()

  x = adj_list_from_fn(pts, adj_fn)
  G = nx.Graph(x)

  return(len(list(nx.connected_components(G))))


def part2(rows, iobj):
  return '*'

print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
