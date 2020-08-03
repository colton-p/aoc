#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def parse(iobj):


  return 


class Intcode:
  def __init__(self, listing):
    self.listing = list(listing)
    self.original_listing = tuple(listing)
    self.pc = 0

  def reset(self):
    self.pc = 0
    self.listing = list(self.original_listing)

  def run_one(self):
    ll = self.listing
    pc = self.pc
    op = ll[pc]

    if op == 1: # add
      (r1, r2, dst) = ll[pc+1:pc+4]

      ll[ dst ] = ll[r1] + ll[r2]
      pc += 4
    elif op == 2: # mult
      # r r dr
      (r1, r2, dst) = ll[pc+1:pc+4]

      ll[ dst ] = ll[r1] * ll[r2]
      pc += 4
    elif op == 3:
      #### HERE
      pass
    elif op == 4:
      #### HERE
      pass
    elif op == 99: #end
      self.pc = None
      return False
    else:
      assert False, "Invalid op code %d at pc %d" % (op, pc)

    self.pc = pc

    return True

  def run_g(self, input_dict={}):
    for k,v in input_dict.items():
      self.listing[k] = v

    while (self.run_one()):
      yield(self.pc, self.listing)

  def run(self, input_dict={}):
    for state in self.run_g(input_dict):
      pass

    return self.listing[0]


def part1(rows, iobj):
  ll = iobj.ints()

  pp = Intcode(ll)

  rslt = pp.run({1: 12, 2: 2})

  return rslt


def part2(rows, iobj):
  ll = iobj.ints()

  pp = Intcode(ll)
  for x in range(100):
    for y in range(100):
      if pp.run({1:x,2:y}) == 19690720:
        return (100*x +y)
      pp.reset()

  return None


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
