from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
import util.grid2 as gg

YEAR = 2022
DAY = 8

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def ray(G, o_pt, dd):

  rr = 0
  o_v = G[o_pt]
  pt = o_pt
  while True:
    pt = vadd(pt, dd)
    if pt not in G.grid:
      return rr
    if G[pt] >= o_v:
      return rr + 1
    
    rr += 1

def part1(rows, iobj):

  G = gg.FixedGrid.from_rows(rows)

  c = 0
  for pt in G.grid:
    rslt = any(ray(G, pt, dd) for dd in [DIR.RIGHT, DIR.LEFT, DIR.UP, DIR.DOWN])
    #if 0 not in pt and 4 not in pt:
    #  print(pt, G[pt], rslt)
    if rslt:
      c += 1

  return c

def part2(rows, iobj):
  G = gg.FixedGrid.from_rows(rows)

  best = 0
  for pt in G.grid:
    score = 1
    for dd in [DIR.RIGHT, DIR.LEFT, DIR.UP, DIR.DOWN]:
      rslt = ray(G, pt, dd)
      score *= rslt
    
    best = max(score, best)
  

  return best
  return

# util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
