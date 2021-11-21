from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 21

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()


def f(L, M, alg):
  ings = [x[0] for x in L if alg in x[1]]  

  return set.intersection(*ings) - set(M.keys())

def parse(rows):
  L = []
  for row in rows:
    l, r = row.split('(contains ')
    ing = set(l.strip().split(' '))
    alg = set(r[:-1].split(', '))
    L += [ (ing, alg) ]
  
  all_alg = set(itertools.chain(*[x[1] for x in L]))
  all_ing = set(itertools.chain(*[x[0] for x in L]))

  M = {}
  for i in range(10):
    for alg in all_alg:
      r = f(L, M, alg)
      if len(r) == 1:
        ing = list(r)[0]
        M[ing] = alg
  
  return L, M

def part1(rows, iobj):

  L, M = parse(rows)

  all_ing = set(itertools.chain(*[x[0] for x in L]))
  safe_ing = all_ing- set(M.keys())

  C = Counter(' '.join(rows).split(' '))

  return sum(C[k] for k in safe_ing)

def part2(rows, iobj):
  L, M = parse(rows)

  return ','.join(sorted(M, key=lambda k: M[k]))

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
