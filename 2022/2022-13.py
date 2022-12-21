from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 13

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def comp(left, right):
  if type(left) == int and type(right) == int:
    if left == right:
      return None
    return left < right

  
  if type(left) == int:
    left = [left]
  if type(right) == int:
    right = [right]
  

  for (l, r) in zip(left, right):
    x = comp(l, r)
    if x is not None:
      return x
    
  if len(left) == len(right):
    return None
  
  return len(left) < len(right)

import functools

def mycomp(left, right):
  r = comp(left, right)

  if r is None: return 0
  if r is True: return -1
  if r is False: return 1
  assert False


def part1(rows, iobj):
  c = 0

  packets = []
  for (ix, (left, right)) in enumerate(iobj.line_delimited()):
    left = eval(left)
    right = eval(right)
    packets += [left, right]
    #print(ix+1, comp(left, right))
    #if comp(left, right):
    #  c += (1+ix)

  packets += [ [2], [6] ]

  packets = sorted(packets, key=functools.cmp_to_key(mycomp))

  return (1+packets.index([2])) * (1+packets.index([6]))

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
