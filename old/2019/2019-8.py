#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 8

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ll = iobj.single_string()


  (W, H) = (25, 6)
  A = W * H

  layers = list(each_slice(list(ll), n=A))

  grid = {}
  for x in range(W):
    for y in range(H):
      grid[(x,y)] = 2
  for layer in layers:
    ix = 0
    for y in range(H):
      for x in range(W):
        if grid[(x,y)] == 2:
          grid[(x,y)] = int(layer[ix])
        ix += 1

  for y in range(H):
    for x in range(W):
      if grid[(x,y)] == 1:
        grid[(x,y)] = '#'
      if grid[(x,y)] == 0:
        grid[(x,y)] = ' '
  print_grid(grid)






def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
