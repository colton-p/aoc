from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def count_faces(pts):
  c = 0
  for (u, v) in its.combinations(pts, 2):
    d = vop(u, v, lambda x,y: abs(x-y))
    if d == (0, 0, 1) or d == (0, 1, 0) or d == (1, 0, 0):
      c += 1
  
  return 6 * len(pts) - 2*c

def part1(rows, iobj):

  return count_faces(nts)

DIRS = [
  (0, 0, 1),
  (0, 0, -1),
  (0, 1, 0),
  (0, -1, 0),
  (1, 0, 0),
  (-1, 0, 0),
]
import util.search
def part2(rows, iobj):

  S = (0, 0, 0)
  MAX = 23
  CUBES = set(nts)

  def adj_fn(pt):
    for dd in DIRS:
      adj = vadd(pt, dd)
      if any(v < -1 for v in adj): continue
      if any(v > MAX for v in adj): continue
      if adj in CUBES: continue

      yield adj
  
  x, pr = util.search.dfs(S, adj_fn)

  EXT = set(pr)
  print(len(EXT))

  c = 0
  for (pt, dd) in its.product(nts, DIRS):
    if vadd(pt, dd) in EXT:
      c += 1

  return c

#util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
