from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 22

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def go(A, B):
  a, b = A.pop(0), B.pop(0)

  if a > b:
    A += [a, b]
  else:
    B += [b,a]


class Game():
  def __init__(self, A, B):
    self.A = list(A)
    self.B = list(B)
    self.seen = set()
    self.winner = None

  def play(self):
    while self.A and self.B and self.winner is None:
      self.round()
    
    if self.winner: return self.winner

    if self.A: return 'A'
    if self.B: return 'B'
    assert False


  def round(self):
    key = (tuple(self.A), tuple(self.B))
    if key in self.seen:
      self.winner = 'A'
      return 'A'
    self.seen.add(key)

    a, b = self.A.pop(0), self.B.pop(0)

    if (a <= len(self.A) and b <= len(self.B)):
      g = Game(list(self.A)[:a], list(self.B)[:b])
      a_wins = (g.play() == 'A')
    else:
      a_wins = a > b

    if a_wins:
      self.A += [a, b]
    else:
      self.B += [b,a]






def part1(rows, iobj):
  A, B = iobj.line_delimited()

  A = list(map(int, A[1:]))
  B = list(map(int, B[1:]))

  while A and B:
    go(A, B)

  return sum([ (len(B) -ix)*b for (ix, b) in enumerate(B) ])

def part2(rows, iobj):
  A, B = iobj.line_delimited()

  A = list(map(int, A[1:]))
  B = list(map(int, B[1:]))

  g = Game(A, B)
  g.play()



  print(g.B)
  print(sum([ (len(g.A) -ix)*b for (ix, b) in enumerate(g.A) ]))
  print(sum([ (len(g.B) -ix)*b for (ix, b) in enumerate(g.B) ]))
  return 

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
