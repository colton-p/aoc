from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 3

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()
ww = iobj.word_tuples()

def f(G, slope):
  (x,y) = (0,0)
  (dx, dy) = slope
  
  c = 0
  while (x,y) in G:
    if G[(x,y)] == '#':
      c += 1
    
    x += dx
    x %= len(rows[0])
    y += dy
  
  return c


def part1(rows, iobj):
  G = Grid.from_rows(rows).grid
  
  return f(G, (3, 1))

def part2(rows, iobj):
  G = Grid.from_rows(rows).grid
  p = 1
  for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    p*= f(G, slope)
  return p

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
