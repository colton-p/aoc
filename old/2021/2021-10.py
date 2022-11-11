from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 10

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

M = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

def f(line):
  S = []
  for c in line:
    if c in '([{<':
      S.append(M[c])
    else:
      exp = S.pop()
      if exp != c:
        return c#, exp
    
  return None

def g(line):
  S = []
  for c in line:
    if c in '([{<':
      S.append(M[c])
    else:
      exp = S.pop()
      if exp != c:
        return c#, exp
    
  return reversed(S)



def part1(rows, iobj):
  PTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
  }

  pts = 0
  for line in rows:
    c = f(line)
    if c:
      pts += PTS[f(line)]

  return pts

def part2(rows, iobj):

  rows = [line for line in rows if not f(line)]

  #line ='<{([{{}}[<[[[<>{}]]]>[]]'

  def v(line):
    P = {
      ')': 1,
      ']': 2,
      '}': 3,
      '>': 4,
    }
    pts = 0
    for c in g(line):
      pts *= 5
      pts += P[c]
    
    return pts

  
  scores = sorted([v(line) for line in rows])
  print(len(scores))
  
  return scores[(len(scores) -1) // 2]

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
