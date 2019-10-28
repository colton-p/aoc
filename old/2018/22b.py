#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 22'
print '------'

rows = input_rows('22', test=False)

print 'row count:', len(rows)
print '------'

GEO_INDEX = {}

TARGET = (14,796)
DEPTH = 5355

N = 1000
Nx = 100
Ny = 1000



test = False
if test:
  DEPTH=510
  TARGET=(10,10)
  N = 100
  Nx = 30
  Ny = 80

GEO_INDEX[(0,0)] = 0
GEO_INDEX[TARGET] = 0

for i in range(1+N):
  GEO_INDEX[(0,i)] = (i * 48271)# % 20183
  GEO_INDEX[(i,0)] = (i * 16807)# % 20183


def erosion(x,y):
  return (DEPTH + GEO_INDEX[(x,y)]) % 20183

for x in range(1, 1+N):
  for y in range(1, 1+N):
    GEO_INDEX[(x,y)] = erosion(x-1,y) * erosion(x,y-1)
GEO_INDEX[TARGET] = 0


def graph(Nx, Ny):

  G = {}
  s = 0
  for x in range(0, Nx+1):
    for y in range(0,Ny+1):
      G[(x,y)] = (erosion(x,y) % 3)
  return G

def vertex(G):
  V = [(x, y, "torch") for (x,y) in G.keys()]
  V += [(x, y, "gear") for (x,y) in G.keys()]
  V += [(x, y, "none") for (x,y) in G.keys()]
  V = []
  for (x,y) in G.keys():
    if G[(x,y)] == 0:
      V += [(x,y,'torch')]
      V += [(x,y,'gear')]
    elif G[(x,y)] == 1:
      V += [(x,y,'gear')]
      V += [(x,y,'none')]

    elif G[(x,y)] == 2:
      V += [(x,y,'torch')]
      V += [(x,y,'none')]
  return V

def adj(G, state, Nx, Ny):
  L = []

  (x,y,tool) = state

  geo_adj = rect_adj_bounds((x,y), 0, Nx, 0, Ny)

  if tool == 'gear':
    assert G[(x,y)] in [0,1]
    for (u,v) in geo_adj:
      if G[(u,v)] in [0, 1]:
        L += [((u,v,tool), 1)]

  elif tool == 'torch':
    assert G[(x,y)] in [0,2]
    for (u,v) in geo_adj:
      if G[(u,v)] in [0, 2]:
        L += [((u,v,tool), 1)]
  elif tool == 'none':
    assert G[(x,y)] in [1,2], (x,y,tool, G[(x,y)])
    for (u,v) in geo_adj:
      if G[(u,v)] in [1, 2]:
        L += [((u,v,tool), 1)]

  if G[(x,y)] == 0:
    L += [((x,y, 'torch'), 7)]
    L += [((x,y, 'gear'), 7)]
  elif G[(x,y)] == 1:
    L += [((x,y, 'gear'), 7)]
    L += [((x,y, 'none'), 7)]
  elif G[(x,y)] == 2:
    L += [((x,y, 'torch'), 7)]
    L += [((x,y, 'none'), 7)]
  return L


G = graph(100, 1000)
V = vertex(G)
def go(Nx, Ny):
  ADJ = {}
  for v in V:
    if v[0] <= Nx and v[1] <= Ny:
      ADJ[v] = adj(G, v, Nx, Ny)

  dist, prev = dijkstra2(V, start=(0,0,'torch'), target=TARGET, adjacent_fn = lambda v: ADJ[v])

  print Nx, Ny, len(ADJ), dist[(TARGET[0],TARGET[1],'torch')]


for dx in range(TARGET[0], TARGET[0]*10):
  for dy in range(TARGET[1], TARGET[1]+8):
    go(dx, dy)
