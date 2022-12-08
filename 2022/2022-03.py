from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 3

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  L = [(s[:len(s)//2], s[len(s)//2:]) for s in rows]
  
  SCORE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
  SCORE += SCORE.upper()
  s = 0
  for (a,b) in L:
    (c,) = list(set(a) & set(b))
    print(c, 1+SCORE.index(c))

    s += (1+SCORE.index(c))
    


  return s

def part2(rows, iobj):

  SCORE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
  SCORE += SCORE.upper()
  s = 0
  for (a,b,c) in each_slice(rows, 3):
    (x,) = list(set(a) & set(b) & set(c))

    s += (1+SCORE.index(x))
  return s

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
