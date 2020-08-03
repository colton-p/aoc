#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 9

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
    self.listing = list(listing) + [0 for x in range(1000)]
    self.original_listing = tuple(listing)
    self.pc = 0
    self.counter = 0
    self.rel_base = 0
    self.input = []
    if type(input) == type([]):
      self.input += input
    elif input is not None:
      self.input += [input]
    self.output = []

  def reset(self):
    self.pc = 0
    self.counter = 0
    self.listing = list(self.original_listing)

  def pp_listing(self, input_dict={}, trial_run=True):
    pc_count = defaultdict(int)
    instructions = self.formatted_instructions()


    if trial_run:
      ix = 0
      pc_count[self.pc] += 1
      for state in self.run_g(input_dict):
        pc_count[self.pc] += 1
        ix += 1
        if ix > 100000:
          break


    indents = sorted(set(pc_count.values()) | set([0]))
    for pc in sorted(instructions):
      print('%4d %4d | %s %s' % (pc_count[pc], pc, '..'*(indents.index(pc_count[pc])), instructions[pc]))

    return pc_count

  def formatted_instructions(self):
    ll = self.listing
    pc = 0

    pps = {}
    def _resolve(arg, mode):
      if mode == 0:
        return 'r' + str(arg)
      else:
        return '' + str(arg)
    while pc < len(ll):
      (op, modes) = self._parse_op_code(ll[pc])

      if op in [1, 2, 7,8]:
        (r1, r2, dst) = ll[pc+1:pc+4]
        v1 = _resolve(r1, modes[0])
        v2 = _resolve(r2, modes[1])
        v3 = 'r' + str(dst)
      elif op in [5, 6]:
        (r1, r2) = ll[pc+1:pc+3]
        v1 = _resolve(r1, modes[0])
        v2 = _resolve(r2, modes[1])
      elif op in [3,4]:
        r1 = ll[pc+1]
        v1 = _resolve(r1, modes[0])

      if op == 3:
        pps[pc] = ("INPUT %s" % (v1))
      elif op == 4:
        pps[pc] = ("OUTPUT %s" % (v1))
      elif op == 1:
        pps[pc] = ("%s := %s + %s" % (v3, v1, v2))
      elif op == 2:
        pps[pc] = ("%s := %s * %s" % (v3, v1, v2))
      elif op == 5:
        pps[pc] = ("GOTO %s if %s != 0" % (v2, v1))
      elif op == 6:
        pps[pc] = ("GOTO %s if %s == 0" % (v2, v1))
      elif op == 7:
        pps[pc] = ("%s := 1 if %s < %s else 0" % (v3, v1, v2))
      elif op == 8:
        pps[pc] = ("%s := 1 if %s == %s else 0" % (v3, v1, v2))
      elif op == 9:
        pass
      elif op == 99:
        pps[pc] = ("END")
        pc += 1
      else:
        pps[pc] = ("(data %s)" % (ll[pc]))

      if op in [1, 2, 7,8]:
        pc += 4
      elif op in [5, 6]:
        pc += 3
      elif op in [3,4]:
        pc += 2
      else:
        pc += 1
    return pps


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
    elif mode == 2:
      return self.listing[self.rel_base + arg]
    else:
      assert False

  def run_one(self):
    ll = self.listing
    pc = self.pc

    self.counter+=1

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
      #print('pc', pc, '|', op, v1, v2, 'r'+str(dst))
      if modes[2] == 2:
        dst += self.rel_base
      pc += 4
    elif op in [5, 6]:
      (r1, r2) = ll[pc+1:pc+3]
      v1 = self._resolve_param(r1, modes[0])
      v2 = self._resolve_param(r2, modes[1])
      #print('pc', pc, '|', op, v1, v2, self.listing[:10])
      pc += 3

    # perform op
    if op == 3:
      # input
      arg1 = ll[pc+1]
      if modes[0] == 2:
        arg1 += self.rel_base
      if len(self.input) != 0:
        ll[arg1] = self.input.pop(0)
      else:
        return False

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
    elif op == 9:
      arg1 = ll[pc+1]
      v1 = self._resolve_param(arg1, modes[0])
      self.rel_base += v1
      pc += 2
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




def part1(rows, iobj):

  listing = iobj.ints()
  #listing = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
  pp = Intcode(listing, [2])
  pp.run()
  print(pp.output)

  return


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
