#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 12

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ll = iobj.numeric_tuples()

  adj = { x[0] : x[1:] for x in ll}
  G = nx.Graph(adj)

  for x in nx.connected_components(G):
    if 0 in x:
      return len(x)

  return


def part2(rows, iobj):
  ll = iobj.numeric_tuples()

  adj = { x[0] : x[1:] for x in ll }
  G = nx.Graph(adj)

  return len(list(nx.connected_components(G)))


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
