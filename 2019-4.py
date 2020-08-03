#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 4

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def ok1(x):
  s = str(x)

  if sorted(s) != list(s):
    return False

  return any((a==b) for (a,b) in each_cons(s))

def ok2(x):
  if not ok1(x): return False


  g = itertools.groupby(str(x))

  return any( (len(list(v)) == 2 for (k,v) in g) )



def count_with_pred(lst, pred):
  return sum(1 for x in lst if pred(x))

def part1(rows, iobj):
  low, high = iobj.ints()

  return count_with_pred(range(low,-high), ok1)


def part2(rows, iobj):
  low, high = iobj.ints()

  return count_with_pred(range(low,-high), ok2)


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
