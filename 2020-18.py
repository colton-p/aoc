from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def op_fn(op):
  if op == '+':
    return lambda x,y: int(x)+int(str(y).strip(')'))
  if op == '*':
    return lambda x,y: int(x)*int(str(y).strip(')'))


def ev(L):
  if len(L) == 1:
    return int(L[0])

  left, op = L[:2]
  return op_fn(op)(left, ev(L[2:]))

def ev2(L):
  if len(L) == 1:
    return L[0]
  for (ix, (l, op, r)) in enumerate(each_cons(L, n=3)):
    if op == '+':
      return ev2(L[:ix] + [l+r] + L[ix+3:])

  for (ix, (l, op, r)) in enumerate(each_cons(L, n=3)):
    if op == '*':
      return ev2(L[:ix] + [l*r] + L[ix+3:])



def f(st):
  L = []
  ix = 0
  while ix < len(st):
    c = st[ix]

    ix += 1
    if c == ' ':
      continue
    elif c == '(':
      (dx, M) = f(st[ix:])
      ix +=dx
      L += [M]
      continue
    elif c == ')':
      break
    else:
      L += [safe_int(c)]

  return (ix, ev2(list(reversed(L))))




def part1(rows, iobj):

  t = {}

  
  return quantify(rows, lambda x: f(x)[1])

def part2(rows, iobj):
  s = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
  return f(s)[1]


util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
