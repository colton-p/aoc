from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 20

iobj = Input.for_date(DAY, year=YEAR, test=False)
#iobj.peek()
#iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()


def part1(rows, iobj):
  (alg, gg) = iobj.line_delimited()
  alg = alg[0]
  G0 = Grid.from_rows(gg)

  def alg_ix(G, pt):
    s = ''
    adj_pts = sorted(list(G.adj_k(pt, diag=True)) + [pt], key=lambda x: (x[1], x[0]))
    for k in adj_pts:
      v = G.grid[k]
      if v == '#':
        s+= '1'
      else:
        s+='0'
    return int(s, 2)


  def ev(G):
    if G.default == '.':
      de = alg[0]
    else:
      de = alg[-1]
    H = Grid.from_rows([[]],default=de)

    # pts = set(itertools.chain(*(G.adj_k(p) for p in list(G.grid.keys()))))

    dd = 4
    for x in range(G.min_x()-dd, G.max_x() +dd):
      for y in range(G.min_y()-dd, G.max_y() +dd):
        pt = (x,y)
        ix = alg_ix(G, pt)
        H.grid[pt] = alg[ix]
    
    return H

  G = G0
  dd = 5


  for i in range(50):
    G[(G.min_x()-dd, G.min_y()-dd)]
    G[(G.min_x()-dd, G.max_y()+dd)]
    G[(G.max_x()+dd, G.max_y()+dd)]
    G[(G.max_x()+dd, G.min_y()-dd)]
    print(i, G.count('#'), G.dims())
    G = ev(G)

  return G.count('#')

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
