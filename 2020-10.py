from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 10

iobj = Input.for_date(DAY, year=YEAR, test=True)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

import util.search as sss

L = list(iobj.int_list()) + [3+max(iobj.int_list())]

#ADJ = {}
#adj_fn = lambda x: [i for i in L if i - x in [1,2,3]]
#ADJ[0] = adj_fn(0)
#for x in L:
#  ADJ[x] = adj_fn(x)

def f(path, node):
  path = path + [node]
  for adj in ADJ[node]:
    r = f(path, adj)
    if r:
      return r
  

  if path == list([0] + sorted(L)):
    c1, c3 = 0, 0
    for (x,y) in each_cons(sorted(path)):
      if abs(x-y) == 1:
        c1 += 1
      elif abs(x-y) == 3:
        c3 += 1
    print(c1 * c3, c1, c3)

    print(path)
    return c1*c3

def g(path, left):
  node = path[-1]
  
  for step in [1,2,3]:
    adj = node + step
    if adj not in left:
      continue
    r = g(path + [adj], left - set([adj]))
    if r: return r

  if not left:
    return path

def val(path):
    c1, c3 = 0, 0
    for (x,y) in each_cons(sorted(path)):
      if abs(x-y) == 1:
        c1 += 1
      elif abs(x-y) == 3:
        c3 += 1
    return c1 * c3

def part1(rows, iobj):
  #path = [0]
  #left = set(L)
  #path = g(path, left)
  #return val(P)

  LL = iobj.int_list()

  # AHHHH JUST SORT THE LIST
  P = [0] + sorted(LL) + [max(LL)+3]
  C = Counter([y-x for (x,y) in each_cons(P)])
  return C[1] * C[3]

def part2(rows, iobj):

  L = sorted(iobj.int_list()) + [max(iobj.int_list())+3]
  D = {k: None for k in L}
  D[0] = 1

  for n in sorted(L):
    D[n] = D.get(n-1, 0) + D.get(n-2, 0) + D.get(n-3, 0)

  return D[max(L)]

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
