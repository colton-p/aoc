#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

from util.intcode import *

YEAR = 2019
DAY = 19

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ll = iobj.ints()



  c = 0
  for x in range(50):
    for y in range(50):
      pp = Intcode(ll)
      pp.input += [x, y]
      pp.run()
      if pp.output[-1] == 1:
        c += 1


  return c


def part2(rows, iobj):
  ll = iobj.ints()
  print(len(D))

  def get(x,y):
    if (x,y) in D:
      return D[(x,y)]
    else:
      pp = Intcode(ll)
      pp.input += [x, y]
      pp.run()
      D[(x,y)] = pp.output[-1]
    return D[(x,y)]


  def chk(x0,y0, dd=100):
    for x in range(x0, x0+dd):
      for y in range(y0, y0+dd):
        if get(x,y) != 1:
          return False
    print('!!!', x0,y0)
    return True


 # for y in range(1000):
 #   chk(2*y,y,dd=100)

  X = 1404
  Y = 699
  for x in range(X-50, X+50):
    for y in range(Y-50, Y+50):
      chk(x,y)

  #print_grid(D)

  return


# print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))