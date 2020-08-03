#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

from util.intcode import *

YEAR = 2019
DAY = 16

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def pattern(ix):
  base = [0,1,0,-1]

  first = True
  it = itertools.cycle(base)

  while True:
    x = next(it)
    for i in range(ix):
      if first:
        first = False
      else:
        yield x

def f(x):
  return abs(x) % 10


def part1(rows, iobj):
  ll = iobj.single_string()
  # ll = '03036732577212944063491565474664'

  offset = int(ll[:7])
  print(offset, len(ll))

  oll = list(map(int, ll))

  ll = []
  for i in range(10000):
    ll += oll
  print(len(ll))
  # pp = Intcode(ll)


  for ph in range(100):
    print('phase', ph)

    out = [0 for i in range(len(ll))]
    #for ix in range(offset, len(ll)):#enumerate(ll):
    V = 0
    for ix in range(len(ll)-1, offset-1, -1):#enumerate(ll):
      V += (ll[ix] % 10)
      # print([(x,y) for (x,y) in zip(ll, itertools.cycle(pattern(ix+1)))])
      out[ix] += f(V)
      # out[ix] = f(sum((x*y % 10) for (x,y) in zip(ll, itertools.cycle(pattern(ix+1)))))
      #for (jx, k) in enumerate(itertools.cycle(pattern(ix+1))):
      #  if jx >= len(ll):
      #    break
      #  out[ix] += (ll[jx] * k) % 10
      #out[ix] = f(out[ix])
      #out+= [f(sum([(x*y) for (x,y) in zip(ll, itertools.cycle(pattern(ix+1)))]))]

    #print(out)
    #print('----')
    ll = out

  return out[offset:offset+8]


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
