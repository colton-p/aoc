from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 15

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()
ll = iobj.ints()

def f():
  said = {
  }
  c = 0
  for i in ll:
    c += 1
    said[i] = (c, None)
    yield i
    last = i

  while c < 200200000:
    c += 1
    (a, b) = said[last]
    #print(c, last, (a,b), said)
    if b is not None:
      spoken = a - b
      (x,y) = said.get(spoken, (None, None))
      said[spoken] = (c, x)
    else:
      spoken = 0
      (x,y) = said.get(spoken, (None, None))
      said[spoken] = (c, x)
    yield (c,spoken)

    last = spoken


def part1(rows, iobj):
  ll = iobj.ints()

  said = {
  }
  c = 0
  for i in ll:
    c += 1
    said[i] = (c, None)
    last = i

  while c < 30_000_000:
    c += 1
    (a, b) = said[last]
    #print(c, last, (a,b), said)
    if b is not None:
      spoken = a - b
      (x,y) = said.get(spoken, (None, None))
      said[spoken] = (c, x)
    else:
      spoken = 0
      (x,y) = said.get(spoken, (None, None))
      said[spoken] = (c, x)
    if c % 100_000 == 0:
      print(c, spoken)

    last = spoken


  return spoken



  return

def part2(rows, iobj):

  g = f()
  info = detect_cycle_it(g)
  print(info)

  return predict_cycle_it(info, 30_000_000, g)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
