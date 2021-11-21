from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 16

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()
R = {}

def chk_v(val):
  for ((a,b), (x,y)) in R.values():
    if (a <= val <= b or x <= val <= y):
      return True
  return False

def chk(ticket):
  for v in ticket:
    if not chk_v(v):
      yield v

def chk2(ticket):
  for v in ticket:
    if not chk_v(v):
      return False
  return True

def part1(rows, iobj):
  rules = rows[0:20]

  for r in rules:
    (k, v) = r.split(': ')
    v1, v2 = v.split(' or ')

    R[k] = ( pints(v1), pints(v2) )

  mine = ints(rows[22])
  tickets = list(map(ints,rows[25:]))

  return sum(itertools.chain(*(chk(t) for t in tickets)))


def candidates(val):
  for (k, ((a,b), (x,y))) in R.items():
    if (a <= val <= b or x <= val <= y):
      yield k
  return

def part2(rows, iobj):
  rules = rows[0:20]

  for r in rules:
    (k, v) = r.split(': ')
    v1, v2 = v.split(' or ')

    R[k] = ( pints(v1), pints(v2) )

  mine = ints(rows[22])
  tickets = list(map(ints,rows[25:]))

  tickets = [t for t in tickets if chk2(t)]

  M = {}

  d = {}
  for pos in range(len(mine)):

    for t in tickets:
      if pos not in d:
        d[pos] = set(candidates(t[pos]))
      else:
        d[pos] = d[pos] & set(candidates(t[pos]))

  while any(d.values()):
    ((tgt_ix,tgt_s),) = [(k,v) for (k,v) in d.items() if len(v) == 1]

    tgt = list(tgt_s)[0]
    M[tgt] = tgt_ix
    print(tgt, tgt_ix)

    for k in d:
      d[k] = d[k] - set([tgt])
    
  ixs = [v for (k,v) in M.items() if 'departure' in k]
  return prod([mine[ix] for ix in ixs])

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
