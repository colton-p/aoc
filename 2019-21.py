#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
from util.intcode import *

YEAR = 2019
DAY = 21

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def must_not_jump(g):

  #     ##.# .#..

  ix = -1
  if g[ix+4] == '.':
    return True
  if g[ix+8] == '.':
    return True
  return False


def part1(rows, iobj):
  if True:
    ll = iobj.ints()
    pp = Intcode(ll)
    # (not c and d) or (not a)
    pp.input += [ord(c) for c in 'NOT A J\n']
    pp.input += [ord(c) for c in 'NOT C T\n']
    pp.input += [ord(c) for c in 'AND H T\n']
    pp.input += [ord(c) for c in 'OR T J\n']
    pp.input += [ord(c) for c in 'NOT B T\n']
    pp.input += [ord(c) for c in 'AND A T\n']
    pp.input += [ord(c) for c in 'AND C T\n']
    pp.input += [ord(c) for c in 'OR T J\n']
    pp.input += [ord(c) for c in 'AND D J\n']
    pp.input += [ord(c) for c in 'RUN\n']
    pp.run()
    print(pp.counter)
    print(pp.output[-1])
    for c in pp.output:
      print(chr(c), end='')

  return


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
#print('P2', part2(rows, iobj))

#for x in itertools.product('#.', repeat=9):
#  print(x, must_not_jump(x))


##.
###
###
#.#


#### no
###.
##.#
#.#.

#not B and D
