from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def chk(range, lx, pw):
  lx = lx.strip(':')
  low, high = map(int, range.split('-'))

  C = Counter(pw)

  return low <= C[lx] <= high

def chk2(range, lx, pw):
  lx = lx.strip(':')
  low, high = map(int, range.split('-'))

  C = Counter(pw)

  a,b = pw[low-1] == lx, pw[high-1] == lx

  return (a or b) and (not a or not b)

def part1(rows, iobj):

  return quantify(tt, lambda x: chk(*x))

def part2(rows, iobj):

  return quantify(tt, lambda x: chk2(*x))

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
