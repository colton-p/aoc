#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 6

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):

  G = nx.Graph()
  ll = iobj.tuples(split=')')

  for (s,t) in ll:
    G.add_edge(t,s)

  c = 0
  for x in G.nodes():
    c += nx.shortest_path_length(G, x, target='COM')


  print(nx.info(G))

  return nx.shortest_path_length(G, source='YOU', target='SAN')


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
