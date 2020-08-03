#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 7

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

class Intcode:
  """
  >>> Intcode.go([1002,4,3,4,33], None, 4)
  99
  >>> Intcode.go([1101,100,-1,4,0], None, 4)
  99
  >>> listing = [3,225,1,225,6,6,1100,1,238,225,104,0,2,218,57,224,101,-3828,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,26,25,224,1001,224,-650,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,44,37,225,1102,51,26,225,1102,70,94,225,1002,188,7,224,1001,224,-70,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,86,70,225,1101,80,25,224,101,-105,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,101,6,91,224,1001,224,-92,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,61,60,225,1001,139,81,224,101,-142,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,102,40,65,224,1001,224,-2800,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,72,10,225,1101,71,21,225,1,62,192,224,1001,224,-47,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,76,87,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]
  >>> Intcode.go(listing, 1, 'stdout')
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 6069343]
  >>> Intcode.go(listing, 5, 'stdout')
  [3188550]

  >>> Intcode.go([3,9,8,9,10,9,4,9,99,-1,8], 8, 'stdout')
  [1]
  >>> Intcode.go([3,9,8,9,10,9,4,9,99,-1,8], 7, 'stdout')
  [0]
  >>> Intcode.go([3,9,7,9,10,9,4,9,99,-1,8], 7, 'stdout')
  [1]
  >>> Intcode.go([3,9,7,9,10,9,4,9,99,-1,8], 9, 'stdout')
  [0]
  >>> Intcode.go([3,3,1108,-1,8,3,4,3,99], 8, 'stdout')
  [1]
  >>> Intcode.go([3,3,1108,-1,8,3,4,3,99], 7, 'stdout')
  [0]
  >>> Intcode.go([3,3,1107,-1,8,3,4,3,99], 7, 'stdout')
  [1]
  >>> Intcode.go([3,3,1107,-1,8,3,4,3,99], 9, 'stdout')
  [0]
  >>> Intcode.go([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0, 'stdout')
  [0]
  >>> Intcode.go([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1, 'stdout')
  [1]
  >>> Intcode.go([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0, 'stdout')
  [0]
  >>> Intcode.go([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1, 'stdout')
  [1]
  >>> listing = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
  >>> Intcode.go(listing, 7, 'stdout')
  [999]
  >>> Intcode.go(listing, 8, 'stdout')
  [1000]
  >>> Intcode.go(listing, 9, 'stdout')
  [1001]
  >>> Intcode.go([3, 9, 3, 10, 1, 9, 10, 0, 99, 0, 0], [123, -23], 0)
  100

  """
  @classmethod
  def go(cls, listing, input=None, ret=0):
    pp = Intcode(listing, input)
    pp.run()

    if ret == 'stdout':
      return pp.output

    return pp.listing[ret]

  def __init__(self, listing, input=None):
    self.listing = list(listing)
    self.original_listing = tuple(listing)
    self.pc = 0
    self.input = []
    if type(input) == type([]):
      self.input += input
    elif input is not None:
      self.input += [input]
    self.output = []

  def reset(self):
    self.pc = 0
    self.listing = list(self.original_listing)


  def _parse_op_code(self, opcode):
    opcode = str(opcode)
    (rev_modes, op) = (opcode[:-2], opcode[-2:])
    rev_modes = list(map(int, rev_modes))

    modes = defaultdict(lambda: 0, enumerate(reversed(rev_modes)))

    return (int(op), modes)

  def _resolve_param(self, arg, mode):
    if mode == 0:
      return self.listing[arg]
    elif mode == 1:
      return arg
    else:
      assert False

  def run_one(self):
    ll = self.listing
    pc = self.pc

    (op, modes) = self._parse_op_code(ll[pc])

    # exit
    if op == 99:
      self.pc = None
      return False

    # resolve parameters
    if op in [1, 2, 7,8]:
      (r1, r2, dst) = ll[pc+1:pc+4]
      v1 = self._resolve_param(r1, modes[0])
      v2 = self._resolve_param(r2, modes[1])
      pc += 4
    elif op in [5, 6]:
      (r1, r2) = ll[pc+1:pc+3]
      v1 = self._resolve_param(r1, modes[0])
      v2 = self._resolve_param(r2, modes[1])
      pc += 3

    # perform op
    if op == 3:
      # input
      arg1 = ll[pc+1]
      if len(self.input) != 0:
        ll[arg1] = self.input.pop(0)
      else:
        return False

      #print("IN", ll[arg1])

      pc += 2
    elif op == 4:
      # output
      arg1 = ll[pc+1]
      v1 = self._resolve_param(arg1, modes[0])
      self.output += [v1]
      #print("OUT", v1)

      pc += 2
    elif op == 1:
      # add
      ll[ dst ] = v1 + v2
    elif op == 2:
      # mult
      ll[ dst ] = v1 * v2
    elif op == 5:
      # ne
      if v1 != 0: pc = v2

    elif op == 6:
      # eq
      if v1 == 0: pc = v2

    elif op == 7:
      # ble
      if v1 < v2: ll[dst] = 1
      else:       ll[dst] = 0
    elif op == 8:
      # beq
      if v1 == v2: ll[dst] = 1
      else:        ll[dst] = 0
    else:
      assert False, "Invalid op code %d at pc %d" % (op, pc)

    self.listing = ll
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



def f(ll, signals):

  ret = ''
  r = 0

  P = {}
  for x in signals:
    P[x] = Intcode(list(ll), [x])

  for x in itertools.cycle(signals):
    pp = P[x]
    pp.input += [r]
    
    #print('in', [x,r])

    #if all((p.pc) is None for p in P.values()):
    if pp.pc is None:
      #print(x, 'halted')
      r = pp.output[-1]
      # print(pp.output)
      continue



    #print(pp.input, pp.pc)
    while (pp.run_one()):
      #print(pp.input, pp.pc)
      pass

    r = pp.output[-1]
    #print('out', r)

    if all((p.pc) is None for p in P.values()):
      break

  print(signals, r)
  return r


def part1(rows, iobj):
  ll = iobj.ints()
  #ll= [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
  #ll = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

  #return f(ll, [9,8,7,6,5])
  #ll = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54, -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4, 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
  #kreturn f(ll, [9,7,8,5,6])

  return max ( f(list(ll), list(x)) for x in itertools.permutations([5,6,7,8,9]) )


  return pp


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
