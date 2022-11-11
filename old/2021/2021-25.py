from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 25

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def ev(G):
  H = Grid(G.grid)
  nrows = 137
  ncols = 139

  pts = list(H.grid.keys())
  for pt in pts:
    if G.grid[pt] != '>': 
      continue
    (x,y) = pt
    adj = ((x + 1) % ncols, y)
    if G.grid[adj] == '.':
      H.grid[adj] = '>'
      H.grid[pt] = '.'

  H1 = Grid(H.grid)

  pts = list(H.grid.keys())
  for pt in pts:
    if H.grid[pt] != 'v': 
      continue
    (x,y) = pt
    adj = (x, (y + 1) % nrows)
    if H.grid[adj] == '.':
      H1.grid[adj] = 'v'
      H1.grid[pt] = '.'
  
  return H1

def part1(rows, iobj):

  G = Grid.from_rows(rows, border_type='hard')
  print(G.to_s())
  print('')

  rslt = detect_constant(G, ev, scoring_func=lambda x:tuple(x.grid.items()), threshhold=1, verbose=True)

  return rslt[0]

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
