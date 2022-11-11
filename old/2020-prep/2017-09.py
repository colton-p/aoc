#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 9

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def eat_garbage(garbage):
  assert garbage[0] == '<'

  cancel = False
  count = 0
  for (ix, c) in enumerate(garbage[1:]):
    if cancel:
      cancel = False
      continue

    if c == '>':
      return (ix + 1, count)
    elif c == '!':
      cancel = True
    else:
      count += 1
      continue

def eat_group(group, lvl=1):
  assert group[0] == '{'
  ix = 1
  score = lvl
  garbage_count = 0
  while ix < len(group):
    c = group[ix]
    if c == '}':
      return (ix+1, score, garbage_count)
    if c == '<':
      (garbage_len, count) = eat_garbage(group[ix:])
      ix += garbage_len
      garbage_count += count
    elif  c == '{':
      (group_len, group_score, gar_count) = eat_group(group[ix:], lvl+1)
      ix += group_len
      score += group_score
      garbage_count += gar_count
    else:
      ix += 1

def part1(rows, iobj):


  return eat_group(iobj.single_string())[1]


def part2(rows, iobj):

  return eat_group(iobj.single_string())[2]


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
