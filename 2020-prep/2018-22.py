#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 22

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.pp_analyze()
rows = list(iobj.rows)

iobj.peak()
(DEPTH,) = iobj.numeric_tuples()[0]
TARGET = tuple(iobj.numeric_tuples()[1])
print(DEPTH, TARGET)


def risk():
  pass

def parse(iobj):

  gindex = {}
  erosion = {}

  for x in range(0, 4*TARGET[0]+1):
    for y in range(0, 100+TARGET[1]+1):
      if x == 0:
        gindex[(x,y)] = (y*48271) % 20183
      elif y == 0:
        gindex[(x,y)] = (x*16807) % 20183
      else:
        gindex[(x,y)] = (erosion[(x-1, y)] * erosion[(x,y-1)])
      gindex[(0,0)] = 0
      gindex[TARGET] = 0

      erosion[(x,y)] = ((DEPTH + gindex[(x,y)]) % 20183)

  ret = {}
  for k in erosion:
    ret[k] = erosion[k] % 3
  return ret

def part1(rows, iobj):
  er = parse(iobj)
  return sum(er.values())


def part2(rows, iobj):

  er = parse(iobj)
  G = nx.Graph()

  TOOLS = ['none', 'torch', 'climb']
  MAX_X = 2*TARGET[0] + 1
  MAX_Y = TARGET[1] + 1
  def is_valid(node):
    (x,y,t) = node
    if er[(x,y)] == 0:
      return t != 'none'
    elif er[(x,y)] == 1:
      return t != 'torch'
    elif er[(x,y)] == 2:
      return t != 'climb'
    else:
      assert False


  nodes = list(itertools.product(range(0, MAX_X), range(0, MAX_Y), ['none', 'torch', 'climb']))
  for (x,y, tool) in nodes:
    if not is_valid((x,y,tool)):
      continue

    for (u,v) in rect_adj_bounds((x,y),0,MAX_X, 0, MAX_Y):
      if is_valid((u,v, tool)):
        G.add_edge((x,y,tool), (u,v, tool), weight=1)

    for t in TOOLS:
      if is_valid((x,y,t)) and t != tool:
        G.add_edge((x,y,tool), (x, y, t), weight=7)

  print(nx.info(G))

  return nx.shortest_path_length(G, (0,0,'torch'), (TARGET[0], TARGET[1], 'torch'), 'weight')


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
