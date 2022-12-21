from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 11

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

class Monkey:
  def __init__(self, block):
    (self.id ,) = ints(block[0])
    self.items = ints(block[1])

    self.count = 0

    op = block[2].split(' ')
    assert op[1] == 'new'
    assert op[2] == '='
    self.op = (op[3:])

    test = block[3].split(' ')
    assert test[1] == 'divisible'
    self.test_val = int(test[3])

    (self.true_tgt,) = ints(block[4])
    (self.false_tgt,) = ints(block[5])
  
  def do_op(self, old):
    (lhs, op, rhs) = self.op

    if lhs == 'old':
      lhs = old
    else:
      lhs = int(lhs)
    if rhs == 'old':
      rhs = old
    else:
      rhs = int(rhs)
    
    if op == '+':
      return lhs + rhs
    elif op == '*':
      return lhs * rhs
    else:
      assert False, self.op
  

  def go(self, MM, NNN):
    if not self.items:
      return False

    o_cur = self.items.pop(0)
    self.count += 1
    cur = self.do_op(o_cur)
    cur = cur % NNN
    #print('\t item %d -> %d' % (o_cur, cur))

    #cur //= 3

    #print('\t div by 3', cur)

    test = (cur % self.test_val) == 0

    #print('\t div by %d' % self.test_val, test)

    if test:
      tgt = self.true_tgt
    else:
      tgt = self.false_tgt
    
    #print('\t tgt', tgt)
    
    MM[tgt].items.append(cur)

    return True


def part1(rows, iobj):

  M = {}
  for block in iobj.line_delimited():
    m = Monkey(block)
    M[m.id] = m
  


  NNN = prod(m.test_val for m in M.values())
  for rr in range(10_000):
    if rr in [1, 20, 1000]:
      for m in M.values():
        print(m.id, m.count)


    for m in M.values():
      #print('---monkey', m.id, '---')
      while m.go(M, NNN):
        pass

  
  
  for m in M.values():
    print(m.id, m.items)



  active = sorted([m.count for m in M.values()], reverse=True)

  return active[0] * active[1]

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
