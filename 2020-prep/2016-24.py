#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2016
DAY = 24

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  grid = Grid.from_rows(rows)
  graph = grid.to_nx(impassable='#')

  labels = { graph.nodes()[n]['label']: n for n in graph.nodes()}

  D = {}
  for (x,y) in itertools.product('12345670', repeat=2):
    D[(x,y)] = nx.shortest_path_length(graph, labels[x], labels[y])

  def ll(path):
    s = 0
    for (a,b) in each_pair(path):
      s += D[(a,b)]
    return s

  paths = ('0' + ''.join(p) + '' for p in itertools.permutations('1234567'))
  return min((ll(p) for p in paths))



def part2(rows, iobj):
  grid = Grid.from_rows(rows)
  graph = grid.to_nx(impassable='#')

  labels = { graph.nodes()[n]['label']: n for n in graph.nodes()}

  D = {}
  for (x,y) in itertools.product('12345670', repeat=2):
    D[(x,y)] = nx.shortest_path_length(graph, labels[x], labels[y])

  def ll(path):
    s = 0
    for (a,b) in each_pair(path):
      s += D[(a,b)]
    return s

  paths = ('0' + ''.join(p) + '0' for p in itertools.permutations('1234567'))
  return min((ll(p) for p in paths))


#print('P1', part1(rows, iobj))
#print('P2', part2(rows, iobj))
import util.output
util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
