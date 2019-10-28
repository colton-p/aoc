from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rows = input_rows('input.txt')

rows = split_rows(rows, sep=' ')

def run(pid):
  REG = collections.defaultdict(int)
  REG['p'] = pid
  REG['__p'] = pid

  pc = 0

  def rrr(x):
    if re.match('[-0-9]+', str(x)):
      return int(x)
    else:
      return REG[x]

  c = 0
  while True:
    c += 1
    row = rows[pc]
    inst = row[0]
    op1 = row[1]
    if len(row) == 3:
      op2 = row[2]
    else:
      op2 = None

    #print pc, row, dict(REG)

    if inst == 'set':
      REG[op1] = rrr(op2)
    elif inst == 'add':
      REG[op1] += rrr(op2)
    elif inst == 'mul':
      REG[op1] *= rrr(op2)
    elif inst == 'mod':
      REG[op1] %= rrr(op2)
    elif inst == 'rcv':
      print '%d rcv  %s' % (REG['__p'], op1)
      val = yield
      print '%d rcv  %s:=%d' % (REG['__p'], op1, val)
      REG[op1] = val
    elif inst == 'snd':
      print '%d snd  %d' % (REG['__p'], rrr(op1))
      yield rrr(op1)
    else:
      assert inst =='jgz', inst

    if inst == 'jgz':
      if REG[op1] > 0:
        pc += rrr(op2)
      else:
        pc += 1
    else:
      pc += 1


r0 = collections.defaultdict(int)
r0['p'] = 0
r0['__p'] = 0
pc0 = 0
inval0 = None
s0 = []

r1 = collections.defaultdict(int)
r1['p'] = 1
r1['__p'] = 1
pc1 = 0
inval1 = None
s1 = []

c = 0
p0 = run(0)
p1 = run(1)


s0 = []

v0 = next(p0)
v1 = next(p1)
for i in range(10):
  while True:
    if v0 is not None:
      s0 += [v0]
      v0 = next(p0)
    elif len(s1) > 0:
      v0 = p0.send(s1.pop(0))
    else:
      break

  print s0, s1

  while True:
    if v1 is not None:
      c += 1
      s1 += [v1]
      v1 = next(p1)
    elif len(s0) > 0:
      v1 = p1.send(s0.pop(0))
    else:
      break

print c
