#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op
import functools

from util import *

YEAR = 2019
DAY = 12

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def apply_gravity(pos, vel):
  for (i,j) in itertools.combinations(range(len(pos)),2):
    for ax in [0,1,2]:
      if pos[i][ax] > pos[j][ax]:
        vel[i][ax] -= 1
        vel[j][ax] += 1
      if pos[i][ax] < pos[j][ax]:
        vel[i][ax] += 1
        vel[j][ax] -= 1

DT = [3, 1, -1, -3]
def sim(t, ax, pos, vel):
  st = t*(t+1)//2
  for (j, ix) in enumerate(sorted(range(len(pos)), key=lambda x: pos[x][ax])):
    pos[ix][ax] = pos[ix][ax] + vel[ix][ax]*t + st*DT[j]
    vel[ix][ax] = vel[ix][ax] + t*DT[j]


def apply_vel(pos, vel):
  for i in range(len(pos)):
    pos[i] = vadd(pos[i], vel[i])

import operator
def eng(pos, vel):
  pot = ([sum(map(abs, x)) for x in pos])
  kin = ([sum(map(abs, x)) for x in vel])

  return sum([x*y for (x,y) in (zip(kin, pot))])

def part1(rows, iobj):
  pos = list(map(list, iobj.numeric_tuples()))
  vel = [[0,0,0] for x in pos]

  print(pos, vel)
  for i in range(1000):
    apply_gravity(pos,vel)
    apply_vel(pos, vel)

  print(pos, vel)
  return eng(pos,vel)


  return

def apply_gravity_axis(pos, vel):
  ret = [0,0,0,0]
  for ix in range(len(ret)):
    dt = sum(-1 for other in pos if other < pos[ix]) + sum(1 for other in pos if other > pos[ix])
    ret[ix] = vel[ix] + dt
  return ret

def apply_vel_axis(pos, vel):
  return vadd(pos, vel)

def g(x,y):
  return x * y // gcd(x,y)


def part2(rows, iobj):
  pos = transpose(iobj.numeric_tuples())
  vel = transpose([[0,0,0] for x in range(4)])

  ret = [0,0,0]
  for ax in [0,1,2]:
    ss = {}

    for i in range(1000000):
      k = tuple(pos[ax] + vel[ax])
      if k in ss:
        print('xyz'[ax], "\t|", ss[k], i)
        ret[ax] = i - ss[k]
        break
      else:
        ss[k] = i

      vel[ax] = apply_gravity_axis(pos[ax], vel[ax])
      pos[ax] = apply_vel_axis(pos[ax], vel[ax])

  print(ret)
  return functools.reduce(g, ret)


# print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
