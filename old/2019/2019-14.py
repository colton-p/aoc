#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 14

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def ff(line):
  (amt, chem) = line.split(' ')
  amt = int(amt)
  return chem, amt


def can_make(need, have):
  return len(need[1] - have) == 0


def part1(rows, iobj):
  D = {}
  for row in rows:
    (lhs, rhs) = row.split(' => ')

    (rslt, qty) = ff(rhs)
    c = Counter()
    for x in lhs.split(', '):
      k,v=ff(x)
      c[k] = v
    D[rslt] = (qty, c)

  reqs = Counter()
  have = Counter()

  import sys
  reqs['FUEL'] = int(sys.argv[1])
  while list(reqs.keys()) != ['ORE']:
    to_make = [k for k in reqs.keys() if k != 'ORE'][0]

    q_need = reqs[to_make]

    (q_made, o_ingredients) = D[to_make]
    copies = math.ceil(q_need / q_made)
    ingredients = Counter()
    for k,v in o_ingredients.items():
      ingredients[k] = v*copies
    q_made *= copies

    reqs[to_make] -= q_made

    reqs += ingredients
    have[to_make] += max((q_made-q_need), 0)

    x,y = (reqs-have, have-reqs)
    reqs = x
    have = y


  
  return (reqs['ORE'] < 1000000000000, reqs['ORE'])


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
