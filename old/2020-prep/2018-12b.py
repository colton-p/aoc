#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2018
DAY = 12

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)



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
    self.generation = 0



  def s_state(self):
    min_ix = min(self.state.keys())
    max_ix = max(self.state.keys())
    return ''.join(self.state[ix] for ix in range(min_ix, max_ix+1))

  def apply_one(self, sub):
    return self.rules.get(sub, self.dead)

  def evolve_one(self):
    ret = defaultdict(lambda: self.dead)

    lookback = ((self.rule_len - 1)//2)

    min_ix = min(self.state.keys())
    max_ix = max(self.state.keys())

    for ix in range(min_ix-lookback, max_ix+lookback+1):
      sub = ''.join([self.state[x] for x in range(ix-lookback, ix+lookback+1)])
      ret[ix] = self.apply_one(sub)

    self.state = ret
    self.generation += 1

    return ret

  def evolve_n(self, n):
    t = self.s0
    for i in range(n):
      yield( self.evolve_one() )

    return t


def parse(iobj):
  s0 = iobj.rows[0].split(':')[1].strip()

  rules = {}
  for k, _, v in iobj.tuples()[2:]:
    rules[k] = v

  return (s0, rules)

parse(iobj)

def part1(rows, iobj):
  s0, rules = parse(iobj)
  ca = CA1(s0, rules)

  c = 0
  for ss in ca.evolve_n(20):
    pass

  return sum([ix for (ix,x) in ca.state.items() if x == '#'])

def part2(rows, iobj):
  s0, rules = parse(iobj)
  ca = CA1(s0, rules)

  def f():
    yield sum([ix for (ix,x) in ca.state.items() if x == '#'])
    for ss in ca.evolve_n(2000):
      #print(sum([ix for (ix,x) in ss.items() if x == '#']))
      yield sum([ix for (ix,x) in ca.state.items() if x == '#'])




  return detect_num_seq(f())(5000000000)


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
