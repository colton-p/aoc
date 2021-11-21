from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 14

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def apply(val, mask):
  bval = "{0:036b}".format(val)
  L = ['']
  for (v, m) in zip(bval, mask):
    #print('\t', v, m, len(L))
    if m == '0':
      L = [s + v for s in L]
    elif m == '1':
      L = [s + '1' for s in L]
    elif m == 'X':
      L = [s + '0' for s in L] + [s + '1' for s in L]

  return [int(s, 2) for s in L]

def part1(rows, iobj):
  M = {}
  mask = ''
  for w in ww:
    if w[0] == 'mask':
      mask = w[1]
    if w[0] == 'mem':
      (_, src, val) = w
      dsts = apply(src, mask)
      for d in dsts:
        M[d] = val
    

  return sum(M.values())

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
