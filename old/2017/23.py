from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rows = input_rows('input.txt')

def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

#grid = rows_to_grid(rows)
#rows = map(int, rows)

#count = count_with_predicate(rows, fff)
#print count

# c = 0
# for row in rows:


# print c

CCC = 0
rows = split_rows(rows, sep=' ')

cond_func = {
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne,
}

def run(REG, pc, val):
  global CCC
  #REG = collections.defaultdict(int)
  #REG['p'] = pid

  SOUNDS_OUT = []
  SOUNDS_IN = []

  def rrr(x):
    try:
      int(x)
      return int(x)
    except ValueError:
      return REG[x]
    #if re.match('[-0-9]+', str(x)):
    #  return int(x)
    #else:
    #  return REG[x]

  c = 0
  if val:
    assert rows[pc][0] == 'rcv'
  while True:
    c += 1
    if pc >= len(rows):
      return CCC
    row = rows[pc]
    inst = row[0]
    op1 = row[1]
    if len(row) == 3:
      op2 = row[2]
    else:
      op2 = None

    if inst == 'set':
      assert op1 != '1', row
      REG[op1] = rrr(op2)
    elif inst == 'sub':
      REG[op1] -= rrr(op2)
    elif inst == 'mul':
      CCC += 1
      REG[op1] *= rrr(op2)
    #elif inst == 'rcv':
    #  if val is None:
    #    #print '%d rcv  %s waiting' % (REG['__p'], op1)
    #    return (REG, pc, val, 'rcv', None)
    #  else:
    #    assert type(val) == type(0), (val, type(val))
    #    #print '%d rcv  %s:=%d' % (REG['__p'], op1, val)
    #    assert op1 != '1', row
    #    REG[op1] = val
    #    val = None
    #elif inst == 'snd':
    #  pc+=1
    #  #print '%d snd  %d' % (REG['__p'], rrr(op1))
    #  return (REG, pc, None, 'snd', rrr(op1))
    else:
      assert inst =='jnz', inst

    if inst == 'jnz':
      chk = rrr(op1)
      if chk != 0:
        pc += rrr(op2)
      else:
        pc += 1
    else:
      pc += 1


r = collections.defaultdict(int)
r['a'] = 0
r['b'] = 4
r['c'] = 21

run(r, 0, None)
for k in sorted(r.keys()):
  print k, r[k]
print r['h']


"""
r1 = collections.defaultdict(int)
r1['p'] = 1
r1['__p'] = 1
pc1 = 0
inval1 = None
s1 = []

c = 0

waiting0 = False
waiting1 = False
for i in range(10000):
  if waiting0 and waiting1:
    break
  #print ''

  #print ''
  #print '<--', pc1, inval1
  while not waiting1:
    (r1, pc1, inval1, x1, outval1) = run(r1, pc1, inval1)
    #print '-->', pc1, inval1, x1
    if x1 == 'snd':
      c += 1
      s1 += [outval1]
      waiting0 = False
    elif x1 =='rcv':
      if len(s0) > 0:
        #waiting1 = False
        inval1 = s0.pop(0)
      else:
        waiting1 = True
    else:
      assert False

  while not waiting0:
    (r0, pc0, inval0, x0, outval0) = run(r0, pc0, inval0)
    if x0 == 'snd':
      s0 += [outval0]
      waiting1 = False
    elif x0 =='rcv':
      if len(s1) > 0:
        #waiting0 = False
        inval0 = s1.pop(0)
      else:
        waiting0 = True
    else:
      assert False


print c
"""
