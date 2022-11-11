from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
import time

YEAR = 2021
DAY = 11

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()


def ev(G):
  for k in G.grid:
    G.grid[k] += 1
  
  flashed = set()
  to_flash = {k for k in G.grid if G.grid[k] > 9}

  while flashed < to_flash:
    for k in to_flash:
      if k not in flashed:
        flashed.add(k)
        for adj in G.adj_k(k):
          G.grid[adj] += 1
    to_flash = {k for k in G.grid if G.grid[k] > 9}
  
  for k in to_flash:
    G.grid[k] = 0
  
  return len(flashed)
  




def part1(rows, iobj):

  G = Grid.from_rows([[int(c) for c in r] for r in rows], border_type='hard')


  #H = ev(G)
  c = 0
  for i in range(1000):
    x = ev(G)
    print(i)
    print(G.to_s())
    y = 1
    for v in range(1000000):
      y *= math.sin(y)

    if x == len(G.grid):
      return i+1

  print(c)


  return c

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
