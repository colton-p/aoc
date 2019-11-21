#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 12

# TODO: how smart to make this?
rows = input_rows(DAY, year=YEAR)

(kind, n_rows, max_row, min_row, _x) = analyze_input(rows)
print("  Kind: %s" % kind)
print("n rows: %4d" % n_rows)
if min_row == max_row:
  print("n cols: %4d" % (max_row))
else:
  print("n cols: %d-%d" % (min_row, max_row))
print('.' * 16)
print('')


rows = input_as_numeric_tuples(DAY, year=YEAR)

import networkx as nx


def part1(rows):
  adj = dict([x[0], x[1:]] for x in rows )

  G = nx.Graph(adj)

  return [len(cc) for cc in nx.connected_components(G) if 0 in cc]


def part2(s):
  adj = dict([x[0], x[1:]] for x in rows )

  G = nx.Graph(adj)

  return(len(list(nx.connected_components(G))))


print('P1', part1(rows))
print('P2', part2(rows))
