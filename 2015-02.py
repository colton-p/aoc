#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2015
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  s = iobj.numeric_tuples()

  return sum([min([l*w, w*h, h*l]) + 2*l*w + 2*w*h + 2*h*l for (l,w,h) in s])


def part2(rows, iobj):
  s = iobj.numeric_tuples()

  return sum([
    sum(min( [(l,w), (w,h), (l,h)], key=lambda x: x[0]*x[1])) * 2 + l*w*h
  for (l,w,h) in s])

print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
