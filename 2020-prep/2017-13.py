#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 13

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):

  d = { k:v for (k,v) in iobj.numeric_tuples()}

  def pos(t):
    return [(depth + t) % range for (depth, range) in d.items()]

  def sev(x, t=0):
    (depth, range) = x

    if (t+depth) % (2*range - 2) == 0:
      return depth * range
    return 0
  
  return quantify(d.items(), sev)
  


  return pos(0)


def part2(rows, iobj):
  d = { k:v for (k,v) in iobj.numeric_tuples()}

  def sev(x, t=0):
    (depth, range) = x

    if (t+depth) % (2*range - 2) == 0:
      return depth * range
    return None

  t = 0
  while True:

    if all(sev(x, t=t) is None for x in d.items()):
      return t
    t += 1
    
  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
