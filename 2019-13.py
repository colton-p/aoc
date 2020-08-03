#!/usr/bin/env python

_input = input

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

from util.intcode import *

YEAR = 2019
DAY = 13

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def ball_dir(ball_pos):
  if len(ball_pos) < 2:
    return None
  return vsub(ball_pos[-1], ball_pos[-2])[0]


def part1(rows, iobj):
  ll = iobj.ints()

  pp = Intcode(ll, [])
  pp.input += []

  pp.run({0: 2})

  G = defaultdict(lambda: '.')
  out = pp.output
  for (x,y, tid) in each_slice(out, n=3):
    if tid == 0:
      tid = ' '
    G[(x,y)] = tid

  scores = []
  blocks = []

  balls = []

  old_score = 0
  old_blocks = [ k for k in G if G[k] == 2 ]

  while True:

    G = defaultdict(lambda: '.')
    out = pp.output
    for (x,y, tid) in each_slice(out, n=3):
      if tid == 0:
        tid = ' '
      G[(x,y)] = tid

    new_score = G[(-1,0)]
    new_blocks = [ k for k in G if G[k] == 2 ]

    if old_score != new_score:
      print('score change!', old_score, new_score)
      scores += [new_score]
      dead_blocks = set(old_blocks) - set(new_blocks)
      print(dead_blocks)
      blocks += list(dead_blocks)
    old_score = new_score
    old_blocks = new_blocks

    print_grid(G)
    print(G[(-1,0)])
    print('')

    (ball_pos,) = [ k for k in G if G[k] == 4 ]
    (paddle_pos,) = [ k for k in G if G[k] == 3 ]

    balls += [ball_pos]

    #print(balls)
    #print(ball_dir(balls))

    dd = ''#_input()
    if dd == '1':
      dd = -1
    elif dd == '3':
      dd = 1
    else:
      if ball_pos[0] < paddle_pos[0]:
        dd = -1
      elif ball_pos[0] > paddle_pos[0]:
        dd = 1
      else:
        dd = 0


      pass

    pp.input += [dd]

    pp.run()


  return sum(1 for x in G.values() if x == 2)


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
