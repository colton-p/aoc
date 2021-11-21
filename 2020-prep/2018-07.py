#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 7

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  G = nx.DiGraph()

  for x in iobj.tuples():
    G.add_edge(x[1], x[-3])


  return (nx.lexicographical_topological_sort(G))


def part2(rows, iobj):
  G = nx.DiGraph()
  for x in iobj.tuples():
    G.add_edge(x[1], x[-3])

  done = []
  working = {}

  for t in range(1000):
    if nx.number_of_nodes(G) == 0 and len(working) == 0:
      return t

    to_start = [n for (n,d) in list(G.in_degree())  if d == 0 and n not in working]
    for n in to_start:
      if len(working) < 5:
        working[n] = 60 + ord(n) - ord('A')+1
    
    for n in working:
      working[n] -= 1
    
    for n in list(working.keys()):
      if working[n] == 0:
        done += [n]
        G.remove_node(n)
        del working[n]
    

print('P1', smart_output(part1(rows, iobj)))
print('P2', smart_output(part2(rows, iobj)))
