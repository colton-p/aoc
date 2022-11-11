from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
from util.search import shortest_path

YEAR = 2021
DAY = 15

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()




def part1(rows, iobj):

  A = Grid.from_rows(rows, border_type='hard')

  print(A.dims())

  (n_x, n_y) = A.dims()
  def f(x0, y0):
    (gx,gy) = (x0 % n_x, y0 % n_y)
    (dx,dy) = (x0 // n_x, y0 // n_y)
    dd = vdist1((0, 0), (dx, dy))

    v = (int(A.grid[(gx, gy)]) + dd)
    while v > 9:
      v = (v-9)

    return v
  
  #for x in range(5*n_y):
    #print(x, f(x, 2))

  #print(f(49, 2))

  G = nx.DiGraph()
  for (x, y) in itertools.product(range(5*n_x), range(5*n_y)):
    pt = (x,y)
    #G.add_node(pt)
    #for adj in A.adj_k(pt, diag=False):
    #for adj in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
    for adj in rect_adj_bounds(pt, 0, 5*n_x-1, 0, 5*n_y-1, diag=False):
      #if adj[0] >= 5*n_x: continue
      #if adj[0] < 0: continue
      #if adj[1] < 0: continue
      #if adj[1] >= 5*n_y: continue

      #v = int(A.grid[adj])
      G.add_edge(pt, adj, weight=f(*adj))
  
  print(nx.info(G))
  dst = (5*n_x-1, 5*n_y-1)
  print(dst)
  print(max(G.nodes()))

  #for (s, t) in each_cons(nx.shortest_path(G, (0, 0), dst, weight='weight')):
  #  pass
    #print(s, t, f(*s), f(*t), G.edges[s, t])
  return nx.shortest_path_length(G, (0, 0), dst, weight='weight')# - int(A.grid[(0,0)]) + int(A.grid[dst])


import functools

def part2(rows, iobj):
  A = Grid.from_rows(rows, border_type='hard')
  (n_x, n_y) = A.dims()
  def f(x0, y0):
    (gx,gy) = (x0 % n_x, y0 % n_y)
    (dx,dy) = (x0 // n_x, y0 // n_y)
    dd = vdist1((0, 0), (dx, dy))

    v = (int(A.grid[(gx, gy)]) + dd)
    if v > 9:
      v = (v-9)

    return v

  def adj_fn(pt):
    for adj in rect_adj_bounds(pt, 0, 5*n_x-1, 0, 5*n_y-1, diag=False):
      yield (adj, f(*adj))

  return shortest_path((0, 0),adj_fn, (5*n_x-1,5*n_y-1))[0]

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
