from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 21

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

DIE = 0
def roll():
  global DIE
  for i in itertools.cycle(range(1, 101)):
    DIE += 1
    yield i

R = roll()

def part1(rows, iobj):

  A = ints(rows[0])[1]
  B = ints(rows[1])[1]
  print(A, B)

  sA = 0
  sB = 0

  for i in range(1000000):
    dA = next(R) + next(R) + next(R)
    A = ((A + dA - 1) % 10) +1
    sA += A

    if sA >= 1000:
      break

    dB = next(R) + next(R) + next(R)
    B = ((B + dB - 1) % 10) +1
    sB += B

    if sB >= 1000:
      break

  print(sA, sB, DIE)
  return min(sA,sB) * DIE

def part2(rows, iobj):

  R_OPTS = ({6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1})

  A = 4
  B = 2
  sA = 0
  sB = 0

  Wa = 0
  Wb = 0
  S = {0: Counter()}


  S[0][(A, sA, B, sB)] += 1
  for i in range(40):
    C = Counter()
    for (state, count) in list(S[i].items()):
      for (roll, n_roll) in R_OPTS.items():
        
        (A, sA, B, sB) = state
        if i % 2 == 0:
          A = ((A + roll - 1) % 10) +1
          sA += A
        else:
          B = ((B + roll - 1) % 10) +1
          sB += B

        C[(A, sA, B, sB)] += count * n_roll

    S[i+1] = Counter()
    for state in C:
      (A, sA, B, sB) = state
      if sA >= 21:
        Wa += C[state]
      elif sB >= 21:
        Wb += C[state]
      else:
        S[i+1][state] = C[state]
    print(i+1, Wa, Wb) 

  return max(Wa, Wb)
  print(W[2] + sum(S[2].values()))
  print(W[3] + sum(S[3].values()))
  print(W[4] + sum(S[4].values()))
  print(W)

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
