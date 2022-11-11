from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 23

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

G = Grid.from_rows(rows)
B = {k:v for (k,v) in G.grid.items() if v in '#'}

BOT = 5

class State:

  def __init__(self, dd) -> None:
      self.dd = dd

  def __str__(self):
    g = Grid({**self.dd, **B})

    return g.to_s() + "\n"

  
  def full_below(self, pt, v):
    (x, y) = pt
    return all(
      self.dd[(x, ty)] == v 
      for ty
      in range(pt[1]+1, BOT+1)
    )
  

  def clear_above(self, pt, v):
    (x, y) = pt
    return all(
      self.dd[(x, ty)] == '.' 
      for ty
      in range(1, y+1, -1)
    )
  
  def home_target(self, pt, v):
    # .   .   .     1
    # .   .   .     2
    # .   A   B     3
    (x,y) = pt
    tgt = None
    for ty in range(2, BOT+1):
      if self.dd[(x, ty)] == '.':
        tgt = (x, ty)
      else:
        break
    if not tgt:
      return

    if not self.full_below(tgt, v):
      return None
    return tgt

  def h(self):

    s = 0
    for (k, v) in self.dd.items():
      if v not in 'ABCD': continue
      ek = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[v]
      tgt_x = {'A': 3, 'B': 5, 'C': 7, 'D': 9}[v]

      (x,y) = k

      s += (2*(4) + abs(x - tgt_x))*ek
    return s


  def tgts_for_pt(self, pt, v):
    (x,y) = pt
    hallway = (y == 1)
    steps = 0
    ek = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[v]
    tgt_x = {'A': 3, 'B': 5, 'C': 7, 'D': 9}[v]

    if x == tgt_x and self.full_below(pt, v):
      # home and full below
      return

    if hallway:
      if x > tgt_x:
        if any(self.dd[(tx, 1)] != '.' for tx in range(tgt_x, x)): return
      elif x < tgt_x:
        if any(self.dd[(tx, 1)] != '.' for tx in range(x+1, tgt_x+1)): return

      home_tgt = self.home_target((tgt_x, 1), v)
      if home_tgt:
        yield home_tgt, (abs(tgt_x-x) + (home_tgt[1] - 1))*ek

    else:
      if not self.clear_above(pt, v):
        return
      
      steps += (y - 1)



      for tx in range(x+1, 12):
        if tx in [3,5,7,9]: continue
        if self.dd[(tx, 1)] == '.':
          yield (tx, 1), (steps + tx-x)*ek
        else:
          break
      for tx in range(x-1, 0, -1):
        if tx in [3,5,7,9]: continue
        if self.dd[(tx, 1)] == '.':
          yield (tx, 1), (steps + x-tx)*ek
        else:
          break


  def adj(self):
    for (pt, v) in self.dd.items():
      if v not in 'ABCD': continue
      for (tgt, energy) in self.tgts_for_pt(pt, v):
        new = dict(self.dd)
        new[pt] = '.'
        new[tgt] = v

        aa = State(dd=new)
        yield aa, energy

    pass

from util.search import shortest_path as sp

def part1(rows, iobj):
  G = Grid.from_rows(rows)
  dd = {k:v for (k,v) in G.grid.items() if v != '#'}

  # GOAL = State({(1, 1): '.', (2, 1): '.', (3, 1): '.', (4, 1): '.', (5, 1): '.', (6, 1): '.', (7, 1): '.', (8, 1): '.', (9, 1): '.', (10, 1): '.', (11, 1): '.', (3, 2): 'A', (5, 2): 'B', (7, 2): 'C', (9, 2): 'D', (0, 3): '.', (1, 3): '.', (3, 3): 'A', (5, 3): 'B', (7, 3): 'C', (9, 3): 'D', (0, 4): '.', (1, 4): '.'})
  GOAL = State({(1, 1): '.', (2, 1): '.', (3, 1): '.', (4, 1): '.', (5, 1): '.', (6, 1): '.', (7, 1): '.', (8, 1): '.', (9, 1): '.', (10, 1): '.', (11, 1): '.', (3, 2): 'A', (5, 2): 'B', (7, 2): 'D', (9, 2): 'D', (0, 3): '.', (1, 3): '.', (3, 3): 'A', (5, 3): 'B', (7, 3): 'C', (9, 3): 'D', (0, 4): '.', (1, 4): '.', (3, 4): 'A', (5, 4): 'B', (7, 4): 'C', (9, 4): 'D', (0, 5): '.', (1, 5): '.', (3, 5): 'A', (5, 5): 'B', (7, 5): 'C', (9, 5): 'D', (0, 6): '.', (1, 6): '.'})
  S0 = State(dd=dd)

  if False:
    for (ix,(x,e)) in enumerate(S0.adj()):
      print(ix, e)
      print(x)
    return

  opt, path = sp(frozenset(S0.dd.items()), lambda x: ((frozenset(a.dd.items()),v) for (a,v) in State(dict(x)).adj()), frozenset(GOAL.dd.items()))
  for x, v in path:
    print('')
    print(v)
    print(State(dict(x)))

  print(opt)


  return
  #S1 = list(S0.adj())[-1][0]
  #S2 = list(S1.adj())[-1][0]
  print(S0)



  return

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
