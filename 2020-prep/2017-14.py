#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 14

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)



def twist(L, position, length):
  orig_L = list(L)
  tgt_idxs = [(position+i) % len(L) for i in range(length)]
  src_idxs = list(reversed(tgt_idxs))

  for (src, tgt) in zip(src_idxs, tgt_idxs):
    L[tgt] = orig_L[src]

  return L
def knot(L, lens, pos=0, skip=0):
  for l in lens:
    L = twist(L, pos, l)
    pos += l + skip
    skip += 1
  
  return (L, pos, skip)
import binascii
def H(input):
  lens = [ord(i) for i in input] + [17, 31, 73, 47, 23]
  pos = skip = 0
  L = list(range(256))
  for _i in range(64):
    (L, pos, skip) = knot(L, lens, pos=pos, skip=skip)
  
  sparse = list(L)
  dense = [0 for i in range(16)]

  import functools
  import operator
  for (ix, block) in enumerate(each_slice(sparse, n=16)):
    dense[ix] = functools.reduce(operator.xor, block)

  return ''.join([bin(x)[2:].zfill(8) for x in dense])

def part1(rows, iobj):
  return quantify((f'{iobj.single_string()}-{i}' for i in range(128)), lambda x: H(x).count('1'))

def part2(rows, iobj):
  grid = {}
  for row in range(128):
    for (col, x) in enumerate(H(f'{iobj.single_string()}-{row}')):
      if x == '1':
        grid[(row, col)] = x
  
  G = nx.Graph()

  # TODO: make grid -> nx
  for k,v in grid.items():
    G.add_node(k)
    for adj in rect_adj(k):
      if adj in grid:
        G.add_edge(k, adj)

  return len(list(nx.connected_components(G)))


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
