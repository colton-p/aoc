#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2015
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):
  G = CA2(rows, survival=[2,3], birth=[3], border='hard')

  G.evolve(100)
  
  return G.number_alive()

def part2(rows, iobj):
  G = CA2(rows, survival=[2,3], birth=[3], border='hard')

  G.grid[(0,0)] = G.grid[(99,0)] = G.grid[(0, 99)] = G.grid[(99, 99)] = '#'
  for _it in range(100):
    G.evolve()
    G.grid[(0,0)] = G.grid[(99,0)] = G.grid[(0, 99)] = G.grid[(99, 99)] = '#'
  
  return G.number_alive()


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
