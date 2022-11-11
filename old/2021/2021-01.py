from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):
  c = 0
  for (x,y) in each_cons(ll):
    if y > x:
      c+=1
  
  return c

def part2(rows, iobj):
  c = 0
  L = list(sum(x) for x in each_cons(ll, n=3))
  for (a,b) in each_cons(L):
    if b > a:
      c += 1

  return c

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
