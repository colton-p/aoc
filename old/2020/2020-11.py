from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 11

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):
  G = Grid.from_rows(rows, border_type='hard')
  
  def evolve(G):
    d = {}
    for pt in G.grid:
      if G[pt] == '.':
        d[pt] = '.'
      elif G[pt] == 'L':
        if sum(1 for i in G.adj_v(pt) if i == '#') == 0:
          d[pt] = '#'
        else:
          d[pt] = 'L'
      elif G[pt] == '#':
        if sum(1 for i in G.adj_v(pt) if i == '#') >= 4:
          d[pt] = 'L'
        else:
          d[pt] = '#'
    return Grid(d, border_type='hard')
  
  val = G.count('#')
  for i in range(100):
    G = evolve(G)
    if val == G.count('#'):
      return val
    val = G.count('#')

def part2(rows, iobj):
  G = Grid.from_rows(rows, border_type='hard')

  dirs = list(grid.rect_adj((0,0), diag=True))
  def adj_cn(G, pt):
      C = 0
      for dir in dirs:
        step = 1
        while True:
          adj = vadd(pt, vscale(dir, step))
          step += 1
          if adj not in G.grid:
            break

          if G.grid[adj] == '.':
            continue

          if G.grid[adj] == '#':
            C += 1
          break
      return C

  def evolve(G):
    d = {}
    for pt in G.grid:
      if G[pt] == '.':
        d[pt] = '.'
      elif G[pt] == 'L':
        if adj_cn(G, pt) == 0:
          d[pt] = '#'
        else:
          d[pt] = 'L'
      elif G[pt] == '#':
        if adj_cn(G, pt) >= 5:
          d[pt] = 'L'
        else:
          d[pt] = '#'
    return Grid(d, border_type='hard')
  
  val = G.count('#')
  for i in range(100):
    G = evolve(G)
    if val == G.count('#'):
      return val
    val = G.count('#')

















def opart1(rows, iobj):

  ca = CA2(rows, survival=[0,1,2,3,4], birth=[0],border='hard')

  ca.print()
  for i in range(1000):
    a = dict(ca.grid)
    ca.evolve()
    b = dict(ca.grid)

    print(i, ca.number_alive())
    #ca.print()

  return ca.number_alive()




  return

def o_part2(rows, iobj):

  ca = CA2(rows, survival=[0,1,2,3,4], birth=[0],border='hard')
  for i in range(100):
    ca.evolve()

    print(i, ca.number_alive())

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
