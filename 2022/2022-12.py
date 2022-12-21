from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
import util.grid2 as ggg

import util.search as sss

YEAR = 2022
DAY = 12

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  G = ggg.FixedGrid.from_rows(rows)

  start = (0, 0)

  goals = [k for (k,v) in G.grid.items() if v in 'Sa']
  (start,) = [k for (k,v) in G.grid.items() if v == 'E']

  def h(x):
    if x  == 'S': return 1
    if x == 'E': return 26
    return ord(x) - ord('a') + 1

  def adj(u):
    cur = h(G[u])
    for v in G.adj_k(u, diag=False):
      #if h(G[v]) <= cur + 1:
      if h(G[v]) >= cur - 1:
        yield (v)

  #print(G.to_s())


  #(v, _) = sss.shortest_path2(start, adj, goal)
  #return v

  def goal_fn(u):
    return G[u] in 'Sa'

  path, pr = sss.bfs(start, adj, goal_fn)

  return len(path) - 1

  for (u, v) in each_cons(path):
    print(G[u], G[v], h(G[u]), h(G[v]))

  for (ix,u) in enumerate(path):
    G.grid[u] = ix
  
  print(G.to_s(cell_size=4))

  return len(path) - 1

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
