from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

from util.search import bfs

YEAR = 2021
DAY = 9

iobj = Input.for_date(DAY, year=YEAR, test=True)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  g = Grid.from_rows(rows, border_type='hard')

  low = []
  for pt in list(g.grid.keys()):
    adj = [int(x) for x in g.adj_v(pt)]
    if all(int(g.grid[pt]) < x for x in adj):
      low += [pt]


  def adj_fn(pt):
    v = g.grid[pt]
    for (adj, adj_v) in g.neighborhood(pt, diag=False).items():
      if int(adj_v) != 9 and int(adj_v) >= int(v):
        yield adj

  print(low)
  basins = [len(bfs(l, adj_fn)[1]) for l in low]
  print(sorted(basins))

  return prod(sorted(basins)[-3:])


  return basins

def part2(rows, iobj):

  G = nx.Graph()
  grid = Grid.from_rows(rows, border_type='hard')
  G.add_nodes_from(grid.grid.keys())

  for s in list(grid.grid.keys()):
    for t in grid.adj_k(s, diag=False):
      if grid.grid[t] == '9': continue
      if grid.grid[s] <= grid.grid[t]:
        G.add_edge(s, t)
    

  return sorted(list(len(c) for c in nx.connected_components(G)))

  return nx.info(G)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
