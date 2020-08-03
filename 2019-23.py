#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
from util.intcode import *

YEAR = 2019
DAY = 23

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ll = list(iobj.ints())
  d = dict()

  q = dict()

  for i in range(50):
    q[i] = []

  for i in range(50):
    pp = Intcode(ll)
    d[i] = pp

    d[i].input += [i]
    d[i].run()

  ss = set()

  for xx in range(100000):

    for i in range(50):
      if q[i]:
        v = q[i].pop(0)
        d[i].input += v
      else:
        d[i].input = [-1]

      d[i].run()
      if d[i].output:
        for (dest, x,y) in each_slice(d[i].output,n=3):
          print(x,y, dest)
          if dest == 255:
            (natx, naty) = (x,y)
          else:
            q[dest].append((x,y))
      d[i].output = []

    if all(len(q[i]) == 0 for i in range(50)):
      print(natx,naty)
      if (natx, naty) in ss:
        print('!!!', naty)
        return naty
      q[0].append((natx, naty))
      ss.add((natx, naty))


  return


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
