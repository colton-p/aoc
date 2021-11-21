from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 17

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def n_adj(G, pt):
  c = 0
  for dx, dy, dz, dw in its.product([-1, 0, 1], repeat=4):
    if dx == dy == dz == dw == 0:
      continue
    pt2 = vadd(pt, (dx, dy, dz, dw))
    if G[pt2] == '#':
      c += 1
  return c

def evolve(G):
  H = defaultdict(lambda: '.')

  adj = defaultdict(int)

  for pt in list(G.keys()):
    adj[pt] = n_adj(G, pt)

  for pt in G.keys():
    if G[pt] == '#' and adj[pt] in [2, 3]:
      H[pt] = '#'
    if G[pt] == '.' and adj[pt] == 3:
      H[pt] = '#'

  return H
  


def part1(rows, iobj):

  G = defaultdict(lambda: '.')
  H = Grid.from_rows(rows)
  for (x,y) in H.grid.keys():
    G[(x,y, 0, 0)] = H[(x,y)]
  

  G = evolve(G)
  

  G = evolve(G)
  G = evolve(G)
  G = evolve(G)
  G = evolve(G)
  G = evolve(G)

  return sum(1 for v in G.values() if v == '#')

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
