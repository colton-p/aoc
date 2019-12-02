#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2016
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

RULES = {
  '...': '.',
  '..^': '^',
  '.^.': '.',
  '.^^': '^',
  '^..': '^',
  '^.^': '.',
  '^^.': '^',
  '^^^': '.',
}

class CA1:
  def __init__(self, s0, rules, dead='.'):
    self.rules = rules
    self.dead = dead

    self.s0 = defaultdict(lambda : dead)
    for (ix, s) in enumerate(s0):
      self.s0[ix] = s

    assert 1 == len( set([len(k) for k in rules]) )
    self.rule_len = len( list(rules.keys())[0] )

    self.state = self.s0


  def apply_one(self, sub):
    return self.rules[sub]
    return self.rules.get(sub, self.dead)

  def evolve_one(self):
    ret = defaultdict(lambda: self.dead)

    lookback = ((self.rule_len - 1)//2)

    min_ix = min(self.state.keys())
    max_ix = max(self.state.keys())

    for ix in range(min_ix-0*lookback, max_ix+0*lookback+1):
      sub = ''.join([self.state.get(x,self.dead) for x in range(ix-lookback, ix+lookback+1)])
      ret[ix] = self.apply_one(sub)

    self.state = ret
    return ret


  def evolve_n(self, n):
    t = self.s0
    yield(t)
    for i in range(n):
      yield(self.evolve_one())

    return t


def part1(rows, iobj):
  ca = CA1(iobj.single_string(), RULES)

  c = 0
  for (ix, ss) in enumerate(ca.evolve_n(40-1)):
    c += sum([1 for x in ss.values() if x == '.'])

  return c

def part2(rows, iobj):
  ca = CA1(iobj.single_string(), RULES)

  c = 0
  for ss in ca.evolve_n(400000-1):
    c += sum([1 for x in ss.values() if x == '.'])

  return c



print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
