#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 4

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def process(rows):
  rows = sorted(rows)

  log = defaultdict(list)
  guard = None
  asleep = None
  for row in rows:
    if 'begins shift' in row:
      guard = ints(row)[-1]

    elif 'falls asleep' in row:
      asleep = ints(row)[-1]

    elif 'wakes up' in row:
      awake = ints(row)[-1]
      log[guard] += [(asleep, awake)]
      asleep = awake = None
    else:
      assert False
  return log


def part1(rows, iobj):
  log = process(rows)
  d = defaultdict(lambda: defaultdict(int))

  for k, v in log.items():
    for (a,b) in v:
      for t in range(a, b):
        d[k][t] += 1
  
  guard = max(d.items(), key=lambda x:sum(x[1].values()))[0]
  minute = max(d[guard].items(), key=lambda x:x[1])[0]
  return guard * minute

def part2(rows, iobj):
  log = process(rows)
  d = defaultdict(int)

  for k, v in log.items():
    for (a,b) in v:
      for t in range(a, b):
        d[(k,t)] += 1
  
  (guard,minute) = max(d.items(), key=lambda x:x[1])[0]
  return guard * minute


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
