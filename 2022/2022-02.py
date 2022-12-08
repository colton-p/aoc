from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=True)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):
  scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

  t = 0

  for (a, b) in tt:
    t += scores[b]
    if scores[a] == scores[b]:
      t += 3
    if (a,b) == ('A', 'Y'): # rock < paper
      t += 6
    if (a,b) == ('A', 'Z'): # rock > scissor
      t += 0
    if (a,b) == ('B', 'X'): # paper > rock
      t += 0
    if (a,b) == ('B', 'Z'): # paper < scissor
      t += 6
    if (a,b) == ('C', 'X'):
      t += 6
    if (a,b) == ('C', 'Y'):
      t += 0


  return t

def part2(rows, iobj):
  scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
  t = 0

  for (a, b) in tt:
    if b == 'Y':
      t += scores[a]
      t += 3
    if b == 'X': # lose
      t += ({'A': 3, 'B': 1, 'C': 2}[a])
    if b == 'Z': # win
      t += ({'A': 2, 'B': 3, 'C': 1}[a])
      t += 6


  return t

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
