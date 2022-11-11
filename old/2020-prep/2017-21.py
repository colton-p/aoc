#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 21

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


R = {}
for row in rows:
  (lhs, rhs) = row.split(' => ')
  R[lhs] = rhs

def enhance(G):
  for H in G.all_orientations():
    k = H.to_s(sep='/')
    if k in R:
      return Grid.from_string(R[k], sep='/')
  print('')
  print(G.to_s())

def update(G):
  H = Grid({})

  if G.nrows() % 2 == 0:
    (a,b) = (2, 3)
  else:
    (a,b) = (3, 4)

  for ((x,y), Gp) in G.subgrids(a, a):
    assert Gp.nrows() == a
    Hp = enhance(Gp)
    assert Hp.nrows() == b
    Hp.translate(x * b, y * b)
    H.grid.update(Hp.grid)

  return H


def part1(rows, iobj):
  G = Grid.from_string('.#./..#/###', sep='/')
  return evolve_n(G, update, 5).count('#')


def part2(rows, iobj):
  G = Grid.from_string('.#./..#/###', sep='/')
  return evolve_n(G, update, 18).count('#')


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
