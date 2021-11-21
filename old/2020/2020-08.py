from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
import util.acccode as ac

YEAR = 2020
DAY = 8

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def go(flip):
  L = list(tt)
  pc = 0
  acc = 0

  if flip is not None:
    (op, val) = L[flip]
    if op == 'jmp':
      L[flip] = ('nop', val)
    elif op == 'nop':
      L[flip] = ('jmp', val)
  
  exec = set()

  while True:

    if pc >= len(L):
      return (True, acc)

    if pc in exec:
      return (False, acc)
    exec.add(pc)

    (op, val) = L[pc]
    if op == 'acc':
      acc += val
      pc += 1
    elif op == 'jmp':
      pc += val
    elif op == 'nop':
      pc += 1
    else:
      assert False, L[pc]
    

def part1(rows, iobj):

  return ac.AccCode.go(iobj.tuples())

  return go(None)

def part2(rows, iobj):

  for (ix, (op, val)) in enumerate(tt):
    pp = ac.AccCode(tt)
    pp.flip_op(ix)
    pp.run()
    if pp.state == 'halted':
      return pp.acc

  return
  for (ix, (op, val)) in enumerate(tt):
    if op in ['jmp', 'nop']:
      (r, answer) = go(ix)
      if r:
        return answer

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
