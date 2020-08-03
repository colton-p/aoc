#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def parse(iobj):


  return 


def f(x,y):
  global iobj
  ll = list(iobj.tuples(',')[0])

  ll[1] = x
  ll[2] = y

  pc = 0

  while True:
    if ll[pc] == 99:
      break
    
    if ll[pc] == 1:
      ll[ ll[pc+3] ] = ll [ ll[pc+1] ] + ll[ ll[pc+2] ]
      # add
    elif ll[pc] == 2:
      ll[ ll[pc+3] ] = ll [ ll[pc+1] ] * ll[ ll[pc+2] ]
      # mult
    else:
      assert False, (ll, pc, ll[pc])
    pc += 4

  ## ll = parse(iobj)

  ## ll = iobj.int_list()

  return ll[0]

def part1(rows, iobj):
  ll = list(iobj.tuples(',')[0])

  ll[1] = 12
  ll[2] = 2

  pc = 0

  while True:
    if ll[pc] == 99:
      break
    
    if ll[pc] == 1:
      ll[ ll[pc+3] ] = ll [ ll[pc+1] ] + ll[ ll[pc+2] ]
      # add
    elif ll[pc] == 2:
      ll[ ll[pc+3] ] = ll [ ll[pc+1] ] * ll[ ll[pc+2] ]
      # mult
    else:
      assert False, (ll, pc, ll[pc])
    pc += 4

  ## ll = parse(iobj)

  ## ll = iobj.int_list()

  return ll[0]


def part2(rows, iobj):

  for x in range(100):
    for y in range(100):
      print(x,y)
      if f(x,y) == 19690720:
        return (100*x +y)

  return None


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
