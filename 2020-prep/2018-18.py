#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def e_pt(val, adj):
  if val == '.':
    if adj.count('|') >= 3:
      return '|'
    else:
      return val

  if val == '|':
    if adj.count('#') >= 3:
      return '#'
    else:
      return val

  if val == '#':
    if adj.count('#') >= 1 and adj.count('|') >= 1:
      return '#'
    else:
      return '.'
  assert False

def evolve(G):
  new = {}
  for pt in G.grid:
    new[pt] = e_pt(G[pt], list(G.neighborhood(pt)))
  
  return Grid(new, border_type='hard')
  
score = lambda x: x.count('#') * x.count('|')

def part1(rows, iobj):
  G = Grid.from_rows(rows, border_type='hard')

  H = evolve_n(G, evolve, 10)

  return score(H)


def part2(rows, iobj):
  G = Grid.from_rows(rows, border_type='hard')

  info = detect_cycle(G, evolve, lambda x: frozenset(x.grid.items()))
  print(info)

  return score(predict_cycle(info, 1000000000))


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
