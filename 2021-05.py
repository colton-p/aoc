from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 5

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):
  pts = [((x,y), (a,b)) for (x,y,a,b) in nts]
  print(pts[0])

  lines = []
  for (p1, p2) in pts:
    (x1, y1) = p1
    (x2, y2) = p2
    if True: #x1 == x2 or y1 == y2:
      lines += [((p1, p2))]

  print(lines[0])
  print(len(lines))

  G = defaultdict(int)

  for (p1, p2) in lines:
    (x1, y1) = p1
    (x2, y2) = p2
    if x1 == x2:
      for y in range(min(y1, y2), max(y1+1,y2+1)):
        G[(x1, y)] += 1
    elif y1 == y2:
      for x in range(min(x1, x2), max(x1, x2)+1):
        G[(x, y1)] += 1
    else:
      dd = vop(vsub(p2, p1), vsub(p2, p1), lambda x, y: x//abs(x))
      p = tuple(p1)
      while p != p2:
        G[p] += 1
        p = vadd(p, dd)
      G[p] += 1
    

  c = 0
  for pt, v in G.items():
    if v >= 2:
      c +=1
  return c




  return

def part2(rows, iobj):

  G = defaultdict(int)
  for (x1, y1, x2, y2) in nts:
    if x1 == x2:
      for y in range (min(y1, y2), max(y1, y2)+1):
        G[(x1, y)] += 1
    elif y1 == y2:
      for x in range (min(x1, x2), max(x1, x2)+1):
        G[(x, y1)] += 1
    else:
      dd = vsub((x2, y2), (x1, y1))
      k = vdist1(dd, (0, 0)) // 2
      dd = vscale(dd, 1/k)
      p = (x1, y1)
      while p != (x2, y2):
        G[p] += 1
        p = vadd(p, dd)
      G[p] += 1

  return quantify(G.values(), lambda v: v >= 2)



  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
