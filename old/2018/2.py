#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

rows = input_rows('2.in')


def f(x,y):
  c = 0
  for (i,j) in zip(x,y):
    if i != j:
      c += 1
  return c == 1

L = []
for row in rows:
  c = Counter(row)
  L += [c]

a = 0
b = 0
for l in L:
  if 2 in l.values():
    a += 1
  if 3 in l.values():
    b += 1
print a
print b
print a*b

for x in rows:
  for y in rows:
    if f(x,y):
      print x
      print y
      

print len(rows)



