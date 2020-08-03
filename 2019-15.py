#!/usr/bin/env python

_input =input

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 15

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

from util.intcode import *

REV = {
  1: 2,
  2: 1,
  3: 4,
  4: 3,
}

VD = {
  1: (0,-1),
  2: (0,1),
  3: (-1,0),
  4: (1,0),
}



def peek(pp, dd):
  pp.input += [dd]
  pp.run()
  if pp.output[-1] == 1:
    return True
  else:
    pp.input += [REV[dd]]
    pp.run()
    return False

def getd():
  x = _input()

  if x == '\x1b[A':
    return 1
  if x == '\x1b[B':
    return 2
  if x == '\x1b[C':
    return 3
  if x == '\x1b[D':
    return 4
  assert False,x



def part1(rows, iobj):
  ll = iobj.ints()

  pp = Intcode(ll)

  G = defaultdict(lambda : ' ')
  pos = (0,0)

  G[pos] = '.'

  TGT = None

  for i in range(10000000):
    dd = random.choice([1,2,3,4])

    pp.input += [dd]
    pp.run()

    if pp.output[-1] == 1:
      G[pos] = '.'
      pos = tuple(vadd(pos, VD[dd]))
      G[pos] = 'D'
    elif pp.output[-1] == 0:
      G[tuple(vadd(pos, VD[dd]))] = '#'
    elif pp.output[-1] == 2:
      G[pos] = '.'
      pos = tuple(vadd(pos, VD[dd]))
      G[pos] = 'X'
      TGT = pos
      print(TGT)
      print_grid(G)

    pp.input = []
    pp.output = []
    #if TGT:
    #  G[TGT] = 'X'
    G[(0,0)] = 'O'

    if i % 100000 == 0:
      print(i)
      print_grid(G)
      print('')

  return

  G[(0,0)] = '.'
  G[TGT] = '.'
  gg = nx.Graph()
  nodes = list(G.keys())
  for k in nodes:
    for adj in rect_adj(k):
      if G[k] == '.' and G[adj] == '.':
        gg.add_edge(k, adj)

  print(nx.info(gg))

  for k in nx.shortest_path(gg, (0,0), TGT):
    G[k] = 'o'
  print_grid(G)
  return nx.shortest_path_length(gg, (0,0), TGT)

XXX = """
#########################################
#.......#.....#.....#.......#.....#.....#
#######.#.###.###.#.###.###.###.#.###.#.#
#.......#.#.......#.#...#.#.....#...#.#O#
#.###.###.#.#######.#.###.#########.#.###
#.#.#.#...#...#...#.#...#...#.....#.#...#
#.#.#.#.#######.#.#.###.###.#.#.#.#.###.#
#.#.#.#.........#.#...#...#...#.#.#...#.#
#.#.#.###########.###.###.#.###.#####.#.#
#.#.....#.......#...#...#.#.#...#.....#.#
#.#####.#####.#####.###.#.###.#.#.#####.#
#.....#.......#...#.#...#.#...#.#.#...#.#
#.###.#####.###.#.#.#.###.#.###.#.#.#.#.#
#...#...#...#...#...#.#...#.#...#.#.#.#.#
#####.#.#.###.#######.#.###.#.###.#.#.#.#
#...#.#.#.#...#.....#...#...#...#.#.#...#
#.#.###.#.#.###.###.#####.#####.#.#.###.#
#.#.....#.#.....#.#...#.....#.#.#.#...#.#
#.#######.#######.###.#.###.#.#.#.###.###
#.......#.#.........#.#.#...#...#...#...#
#.#####.#.#.###.###.#.#.#.###.#####.###.#
#.#.#...#.#.#.#...#.#.#.#.#.......#...#.#
#.#.#.#####.#.###.#######.#######.###.#.#
#.#.#.....#.#...#.........#...#...#.#.#.#
#.#.#####.#.#.#.###.#######.#.#.###.#.#.#
#.....#...#.#.#...#.........#.#...#.#.#.#
###.###.###.#.###.###########.###.#.#.#.#
#.#.#...#...#.#.........#.....#.....#...#
#.#.#.###.#####.#######.#.#####.#######.#
#...#...#.#...#.......#.#.#.....#.......#
#######.#.#.#.#######.###.###.###.#######
#.....#.#.#.#.......#...#...#.#...#.....#
#.###.#.#.#.#######.###.###.#.#.###.#####
#.#.#.#.#.#.......#.....#...#.#...#.....#
#.#.#.#.#.#.#####.#####.#.#######.#####.#
#.#...#.#.#...#...#.....#...#.....#.....#
#.#.###.#.###.#.###########.#.#####.###.#
#.#.....#...#.#...........#.#.#.....#...#
#.#########.###########.#.#.#.###.###.###
#.......................#.#.......#.....#
#########################################
"""

def part2(rows, iobj):

  rows = XXX.strip().split('\n')
  G = rows_to_grid(rows)
  print_grid(G)

  c = 0
  while '.' in G.values():
    oxygens = [k for k in G if G[k] == 'O']
    for oxy in oxygens:
      for v in rect_adj(oxy):
        if G[v] == '.':
          G[v] = 'O'
    c+=1
    print(c)
    print_grid(G)
    print('')


  return c


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
