#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2017
DAY = 15

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def gA1(x):
  while True:
    x = (16807 * x) % 2147483647
    yield x

def gB1(x):
  while True:
    x = (48271 * x) % 2147483647
    yield x

def gA2(x):
  while True:
    x = (16807 * x) % 2147483647
    if x % 4 == 0:
      yield x

def gB2(x):
  while True:
    x = (48271 * x) % 2147483647
    if x % 8 == 0:
      yield x


def compare(a, b):
    a = bin(a)[2:].zfill(32)
    b = bin(b)[2:].zfill(32)
    
    return a[-16:] == b[-16:]

def part1(rows, iobj):
  (xa,) = ints(rows[0])
  (xb,) = ints(rows[1])

  return quantify( zip(range(40_000_000), gA1(xa), gB1(xb)), lambda x: compare(x[1], x[2]) )

def part2(rows, iobj):
  (xa,) = ints(rows[0])
  (xb,) = ints(rows[1])

  return quantify( zip(range(5_000_000), gA2(xa), gB2(xb)), lambda x: compare(x[1], x[2]) )

print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
