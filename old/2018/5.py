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

regex = []
types = set(line.lower())
for t in types:
  regex += [(t + t.upper())]
  regex += [(t.upper() + t)]
REGEX = '|'.join(regex)

def f(line):
  return re.sub(REGEX, '', line)

def g(line):
  return f(line)

def p1(line):
  x = g(line)
  while line != x:
    line = x
    x = g(x)
  return line

D = defaultdict(int)
types = set(line.lower())

for t in types:
  print t, len(p1(line.translate(None, t + t.upper())))


