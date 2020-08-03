#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 22

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def shuffle(deck):
  for instr in rows:
    if instr == 'deal into new stack':
      deck = list(reversed(deck))
    elif instr.startswith('deal with increment'):
      (incr,) = ints(instr)
      new_deck = [None for i in range(len(deck))]

      ix = 0
      for top_card in deck:
        assert new_deck[ix] is None
        new_deck[ix] = top_card
        ix = (ix + incr) % len(deck)
      assert all(x is not None for x in new_deck)

      deck = new_deck

    elif instr.startswith('cut'):
      (incr,) = ints(instr)
      if incr > 0:
        deck = deck[incr:] + deck[:incr]
      else:
        incr = -incr
        deck = deck[-incr:] + deck[:-incr]

  return deck



def part1(rows, iobj):
  N = 10007

  deck = [i for i in range(N)]

  s = set()
  for i in range(1):
    ix = deck.index(2019)
    if ix in s:
      print(i, ix)
      break
    s.add(ix)
    deck = shuffle(deck)

  return deck.index(2019)

def backtrack_ix(N, rows, ix):
  for (op, offset) in reversed(rows):
    if op == 'r':
      ix = (N-1) - ix
    elif op == 'i':
      inv_offset = modinv(offset, N)

      ix = (inv_offset * ix) % N
    elif op == 'c':
      ix = (ix + offset) % N

  return ix

def parse_row(r):
  if r == 'deal into new stack':
    return 'r',0
  elif r.startswith('deal with increment'):
    (offset,) = ints(r)
    return 'i', offset
  elif r.startswith('cut'):
    (offset,) = ints(r)
    return 'c', offset



def find_coeffs(N, rows):
  a = 1
  b = 0

  # c*a*x + (c*b +  d)
  for (op, offset) in reversed(rows):
    if op == 'r':
      (c, d) = (-1, N-1)
    elif op == 'i':
      inv_offset = modinv(offset, N)
      (c, d) = (inv_offset, 0)
    elif op == 'c':
      (c, d) = (1, offset)

    a = c*a % N
    b = (c*b + d) % N

  return (a,b)

def backtrack_ix3(N, ix):
  return (ix * 85650819410793 + 42113960774850) % N


def iter_coeffs(pt, n, N):
  (a,b) = pt
  c = pow(a, n, N)
  d = 0
  for i in range(n):
    d = (d + pow(a, i, N)*b) % N

  return (c,d)

def apply_coeffs(coeffs, n, N, x):
  (a,b) = coeffs

  for i in range(n):
    x = (a*x + b) % N

  return x

import time
def part2a(rows, iobj):
  reps = 101741582076661

  N = 119315717514047
  rows = [parse_row(r) for r in rows]

  G = dict()
  G[0] = find_coeffs(N, rows)
  for exp in range(1, len(str(reps))):
    G[exp] = iter_coeffs(G[exp-1], 10, N)


  t0 = time.time()
  x = 2020
  for (exp, sv) in enumerate(reversed(str(reps))):
    x = apply_coeffs(G[exp], int(sv), N, x)
  print(x)
  print(time.time()-t0)

  
  return

#print('P1', part1(rows, iobj))
print('P2', part2a(rows, iobj))
