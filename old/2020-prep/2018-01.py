from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2018
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

try:
  ss = iobj.single_string()
except:
  ss = None
try:
  ll = iobj.int_list()
except:
  ll = None
try:
  nts = iobj.numeric_tuples()
except:
  nts = None

def part1(rows, iobj):

  return sum(ll)

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
