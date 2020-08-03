#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 24

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def n_adj(G, k):
  c = 0

  for k in my_adj(k):
    if k in G:
      if G[k] == '#':
        c += 1
  return c

def ev(G):
  H = {}#dict(G)
  for k in G:
    if G[k] == '.':
      if n_adj(G, k) in [1,2]:
        H[k] = '#'
      else:
        H[k] = '.'
    elif G[k] == '#':
      if n_adj(G, k) != 1:
        H[k] = '.'
      else:
        H[k] = '#'
    else:
      assert k[0] == 2 and k[1] == 2 and G[k] == '?'
  return H


def my_adj(pt):
  (x,y,lvl) = pt

  # up
  if y == 0:
    yield (2,1, lvl-1)
  elif y == 3 and x == 2:
    yield (0, 4, lvl+1)
    yield (1, 4, lvl+1)
    yield (2, 4, lvl+1)
    yield (3, 4, lvl+1)
    yield (4, 4, lvl+1)
  else:
    yield (x, y-1, lvl)

  # down
  if y == 4:
    yield (2,3, lvl-1)
  elif y == 1 and x == 2:
    yield (0, 0, lvl+1)
    yield (1, 0, lvl+1)
    yield (2, 0, lvl+1)
    yield (3, 0, lvl+1)
    yield (4, 0, lvl+1)
  else:
    yield (x, y+1, lvl)

  # right
  if x == 4:
    yield (3, 2, lvl-1)
  elif x == 1 and y == 2:
    yield(0, 0, lvl+1)
    yield(0, 1, lvl+1)
    yield(0, 2, lvl+1)
    yield(0, 3, lvl+1)
    yield(0, 4, lvl+1)
  else:
    yield (x+1, y, lvl)

  # left
  if x == 0:
    yield (1, 2, lvl-1)
  elif x == 3 and y == 2:
    yield(4, 0, lvl+1)
    yield(4, 1, lvl+1)
    yield(4, 2, lvl+1)
    yield(4, 3, lvl+1)
    yield(4, 4, lvl+1)
  else:
    yield (x-1, y, lvl)

def ppl(G, lvls):
  for i in lvls:
    print('depth', i)
    H = dict()
    H[(2,2)] = '?'
    for k in G:
      (x,y,lvl) = k
      if lvl == i:
        H[(x,y)] = G[k]

    print_grid(H)
    print('')


def part2(rows, iobj):


  G0 = rows_to_grid(rows)
  del G0[(2,2)]

  G = dict()
  for k in G0:
    (x,y) = k
    for lvl in range(-200, 200):
      if lvl != 0:
        G[(x,y,lvl)] = '.'#G0[k]
    G[(x,y,0)] = G0[k]

  for x in my_adj( (1,2,-1) ):
    print(x, G[x])


  ppl(G, [-1,0,1])

  for i in range(200):
    print(i, max(abs(k[2]) for k in G if G[k] == '#'), sum(1 for i in G.values() if i == '#'))
    G = ev(G)

  ppl(G, [-1,0,1])


  return sum(1 for i in G.values() if i == '#')

def part1(rows, iobj):

  s = set()
  G = rows_to_grid(rows)
  print_grid(G)

  print(n_adj(G, (0,0)))

  #G = ev(G)
  #G = ev(G)
  print('')


  for i in range(1):
    gg = tuple(sorted(G.items()))
    if gg in s:
      print('!!!')
      print_grid(G)
      break
    s.add(gg)
    G = ev(G)

  # ll = iobj.int_list()
  cc = 0
  i = 0
  for y in range(5):
    for x in range(5):
      if G[(x,y)] == '#':
        cc += 2**i
      i+=1
  return cc


  return





#print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
