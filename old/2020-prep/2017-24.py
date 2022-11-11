#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 24

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  G = nx.DiGraph()
  #G.add_node('s')
  #G.add_node('t')

  for (x,y) in iobj.numeric_tuples():
    G.add_edge(x,y)
    G.add_edge(y,x)
  
  G.add_node('t')
  for n in G.nodes:
    G.add_edge(n, 't')

  r = 0
  exit()
  for (ix,p) in enumerate(nx.all_simple_paths(G, 0, 't')):
    v = sum(p[:-1])+sum(p[1:-2])
    print(v, p)
    if v > r:
      print(v, p)
      r = v
  return


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
