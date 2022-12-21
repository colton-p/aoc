from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
import util.grid2 as ggg

YEAR = 2022
DAY = 9

iobj = Input.for_date(DAY, year=YEAR, test=1)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  visited = set()
  h = (0, 0)
  t = (0 ,0)
  visited.add(t)


  for (d, v) in tt:
    v = int(v)
    print('==', d, v, '===')
    d = {'U': DIR.UP, 'L': DIR.LEFT, 'R': DIR.RIGHT, 'D': DIR.DOWN}[d]


    for i in range(v):
      print('h', h, 't', t)

      h = vadd(d, h)

      diff = vsub(h, t)
      if abs(max(diff, key=abs)) > 1:
        step = tuple(abs(q) // q if q != 0 else 0 for q in diff)
        t = vadd(t, step)
        print(t)

        visited.add(t)

  return len(visited)

def pp(T):
  g = {pt: ix for (ix, pt) in enumerate(T)}
  g[(0, 0)] = 's'

  G = ggg.OpenGrid(g)

  print(G.to_s(cell_size=3))

def part2(rows, iobj):

  visited = set()
  h = (0, 0)
  t = (0 ,0)

  T = [(0,0) for i in range(10)]

  visited.add(T[-1])

  for (d, v) in tt:
    v = int(v)
    # pp(T)
    print('==', d, v, '===')
    d = {'U': DIR.UP, 'L': DIR.LEFT, 'R': DIR.RIGHT, 'D': DIR.DOWN}[d]


    for _ in range(v):
      # print('h', T[0], 't', T[-1])

      T[0] = vadd(d, T[0])

      for t_ix in range(1, len(T)):
        t = T[t_ix]
        diff = vsub(T[t_ix-1], t)
        if abs(max(diff, key=abs)) > 1:
          step = tuple(abs(q) // q if q != 0 else 0 for q in diff)
          T[t_ix] = vadd(t, step)
          # print(t_ix, t)

          if t_ix == 9:
            visited.add(t)

  pp(visited)

  return len(visited)

  return

#util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
