#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2015
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def _part1(rows, iobj):
  G = rows_to_grid(rows)
  G[(0,0)] = G[(99,0)] = G[(0, 99)] = G[(99, 99)] = '#'
  for it in range(100):
    H = {}
    for k in G:
      nadj = sum(1 for i in rect_adj_bounds(k, 0, 99, 0, 99, diag=True) if G[i] == '#')
      H[k] = '.'
      if G[k] == '#':
        if nadj in [2,3]:
          H[k] = '#'
      else:
        if nadj == 3: H[k] = '#'
    H[(0,0)] = H[(99,0)] = H[(0, 99)] = H[(99, 99)] = '#'
    G = H

  return sum(1 for v in G.values() if v == '#')

def part1(rows, iobj):
  G = CA(rows, survival=[2,3], birth=[3])

  for _it in range(100):
    G.evolve()
  
  return G.number_alive()

def part2(rows, iobj):
  G = CA(rows, survival=[2,3], birth=[3])

  G.grid[(0,0)] = G.grid[(99,0)] = G.grid[(0, 99)] = G.grid[(99, 99)] = '#'
  for _it in range(100):
    G.evolve()
    G.grid[(0,0)] = G.grid[(99,0)] = G.grid[(0, 99)] = G.grid[(99, 99)] = '#'
  
  return G.number_alive()


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
