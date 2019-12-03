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
  def __init__(self, program):
    self.program = list(program)
    self.o_program = tuple(program)


  def reset(self):
    self.program = list(self.o_program)

  def run(self, input_dict):
    pc = 0
    ll = list(self.program) # stateless
    # ll = (self.program) # stateful

    for k,v in input_dict.items():
      ll[k] = v


    while True:
      op = ll[pc]

      if op == 1: # add
        (r1, r2, dst) = ll[pc+1:pc+4]

        ll[ dst ] = ll[r1] + ll[r2]
        pc += 4
      elif op == 2: # mult
        (r1, r2, dst) = ll[pc+1:pc+4]

        ll[ dst ] = ll[r1] * ll[r2]
        pc += 4
     # elif op == 3:
     #   pass
     # elif op == 4:
     #   pass
      elif op == 99: #end
        break
      else:
        assert False, "Invalid op code %d at pc %d" % (op, pc)


    return ll[0]

def part1(rows, iobj):
  ll = iobj.ints()

  pp = Intcode(ll)

  print(pp.program)
  rslt = pp.run({1: 12, 2: 2})
  print(pp.program)

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
