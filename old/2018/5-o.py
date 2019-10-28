#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 5'
print '------'

rows = input_rows('input.txt')

line = rows[0]

print '------'

def f(line):
  i = 0
  while i < len(line)-1:
    (x,y) = line[i], line[i+1]
    if x.lower() == y.lower() and x != y:
      i += 2
      continue
    else:
      yield x
    i += 1
  if i < len(line):
    yield line[i]

def g(line):
  return list(f(line))


def p1(line):
  new_line = g(line)
  while line != new_line:
    line = new_line
    new_line = g(line)
  return line

D = defaultdict(int)
types = set(line.lower())

for t in types:
  print t, len(p1(line.translate(None, t + t.upper())))


