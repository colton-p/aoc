from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 21

iobj = Input.for_date(DAY, year=YEAR, test=False)
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

ops = {}
done = {}

def parse_rows(rows):
  for row in rows:
    (lhs, vals) = row.split(': ')
    rhs = vals.split(' ')
    if len(rhs) == 1:
      ops[lhs] = int(rhs[0])
    else:
      a, oper, b = rhs
      func = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.ifloordiv}[oper]
      ops[lhs] = (oper, func, a, b)
  
  return ops
    
from fractions import Fraction

def part1(rows, iobj):
  ops = parse_rows(rows)
    
  def eval(x):
    if type(ops[x]) == int:
      return ops[x]

    (_, func, a, b) = ops[x]

    return func(eval(a), eval(b))
  return eval('root')

def part2(rows, iobj):
  ops = parse_rows(rows)
    
  def eval(x):
    if x == 'humn':
      return (1, 0)
    if type(ops[x]) == int:
      return (0, ops[x])

    (oper, _, left, right) = ops[x]
    (a,b) = eval(left)
    (c,d) = eval(right)

    if oper == '+':
      return (a + c, b + d)
    if oper == '-':
      return (a - c, b - d)
    if oper == '*':
      assert a * c == 0
      return (a*d + b*c, b*d)
    if oper == '/':
      assert c == 0
      return (Fraction(a, d), Fraction(b,d))

  (oper, func, left, right) = ops['root']

  (a, b) = eval(left)
  (c, tgt) = eval(right)
  assert c == 0

  return (tgt - b) / a


util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
